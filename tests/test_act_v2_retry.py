"""Actual generated Act clients against fake HTTP transports, never providers."""
import asyncio
import copy
import json
import unittest
from unittest.mock import AsyncMock, patch

import httpx
from darwin_sdk import Darwin, AsyncDarwin
from darwin_sdk.core.api_error import ApiError
from darwin_sdk.types.start_thread_body import StartThreadBody_Message
from darwin_sdk.types.send_message_body import SendMessageBody_Message


class ActV2RetryTests(unittest.TestCase):
    def test_all_sync_and_async_writes_keep_one_attempt_with_keys_and_retry_overrides(self):
        for method in ("start_thread", "send_message", "archive_thread", "authenticate", "pay"):
            for identity in ("omitted", "body", "header override"):
                for asynchronous in (False, True):
                    with self.subTest(method=method, identity=identity, asynchronous=asynchronous):
                        calls = []
                        body_key = identity == "body" and method != "archive_thread"
                        header_key = identity == "header override" or (identity == "body" and method == "archive_thread")
                        key = {"idempotency_key": "original-key"} if body_key else {}
                        options = {"max_retries": 5, "additional_headers": {"X-Fixture": "kept"}}
                        if header_key:
                            options["additional_headers"]["Idempotency-Key"] = "original-key"
                        before = copy.deepcopy(options)

                        def respond(request):
                            calls.append(request)
                            return httpx.Response(500, json={"code": "UNKNOWN_AFTER_ACCEPTANCE"})

                        def invoke(client):
                            if method == "start_thread":
                                return client.start_thread(request=StartThreadBody_Message(
                                    target_agent="target_fixture", message_content="Original inquiry", **key), request_options=options)
                            if method == "send_message":
                                return client.send_message("thread_fixture", request=SendMessageBody_Message(
                                    message_content="Original continuation", **key), request_options=options)
                            if method == "archive_thread":
                                return client.archive_thread("thread_fixture", request_options=options)
                            return getattr(client, method)(request="request_fixture", request_options=options, **key)

                        if asynchronous:
                            async def run():
                                async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as transport:
                                    client = AsyncDarwin(api_key="fixture", httpx_client=transport, max_retries=2)
                                    with self.assertRaises(ApiError):
                                        await invoke(client)
                            asyncio.run(run())
                        else:
                            with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
                                client = Darwin(api_key="fixture", httpx_client=transport, max_retries=2)
                                with self.assertRaises(ApiError):
                                    invoke(client)
                        self.assertEqual(len(calls), 1)
                        self.assertEqual(calls[0].method, "POST")
                        self.assertEqual(calls[0].headers["X-Fixture"], "kept")
                        self.assertEqual(calls[0].headers.get("Idempotency-Key"), "original-key" if header_key else None)
                        body = json.loads(calls[0].content)
                        self.assertEqual(body.get("idempotencyKey"), "original-key" if body_key else None)
                        self.assertEqual(options, before)

    def test_sync_and_async_v2_thread_reads_keep_their_retry_budget(self):
        for asynchronous in (False, True):
            calls = []
            snapshot = dict(thread="thread_fixture", messages=[], actions=[], requests=[], errors=[],
                            cursor="thread_fixture:0", hasMore=False, archived=False, needsAttention=False)

            def respond(request):
                calls.append(request)
                self.assertEqual(request.method, "GET")
                return httpx.Response(503, json={"code": "TRANSIENT"}) if len(calls) == 1 else httpx.Response(200, json=snapshot)

            if asynchronous:
                async def run():
                    async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as transport:
                        client = AsyncDarwin(httpx_client=transport, max_retries=1)
                        value = await client.get_thread("thread_fixture")
                        self.assertEqual(value.thread, "thread_fixture")
                with patch("darwin_sdk.core.http_client.asyncio.sleep", new=AsyncMock()):
                    asyncio.run(run())
            else:
                with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
                    client = Darwin(httpx_client=transport, max_retries=1)
                    with patch("darwin_sdk.core.http_client.time.sleep"):
                        self.assertEqual(client.get_thread("thread_fixture").thread, "thread_fixture")
            self.assertEqual(len(calls), 2)

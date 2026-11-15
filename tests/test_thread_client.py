"""Generated SDK wire tests against a loopback HTTP server, not provider proof."""

import asyncio
from contextlib import contextmanager
import json
import os
from pathlib import Path
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
import unittest
import httpx
from unittest.mock import AsyncMock, patch
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from darwin_sdk import Darwin, AsyncDarwin
from darwin_sdk.act.errors.conflict_error import ConflictError as ActConflictError
from darwin_sdk.core.api_error import ApiError
from darwin_sdk.types.send_message_body import SendMessageBody_Message
from darwin_sdk.types.start_thread_body import StartThreadBody_Message


def snapshot():
    return dict(thread="thread-1", messages=[], actions=[], requests=[], cursor="thread-1:0",
                hasMore=False, archived=False, needsAttention=False)


def response(call, count):
    path = urlsplit(call["path"]).path
    if path.endswith("/v3/search"):
        return 200, {
            "searchId": "srch_11111111-1111-4111-8111-111111111111",
            "responseId": "sresp_22222222-2222-4222-8222-222222222222", "previousResponseId": None,
            "contractVersion": "search-v3.0", "status": "no_match",
            "response": {"agents": [], "relatedSearches": [], "plan": None, "question": None,
                         "noMatchReason": "No eligible agent."},
        }
    if path.endswith("/search"):
        return 200, {
            "contractVersion": "search-public-v2",
            "outcome": "NO_ELIGIBLE_SUPPLY",
            "results": [],
            "agents": [],
            "versions": {key: None for key in (
                "generation", "projection", "embedding", "sparse", "retrieval", "feature", "ranker", "policy"
            )},
        }
    if path.endswith("/messages"):
        return 202, dict(thread="thread-1", message="message-1", status="accepted", cursor="thread-1:1",
                         idempotencyKey="message-1")
    if path.endswith("/authentications"):
        return 200, dict(authentication="attempt-1", status="awaiting_consent",
                         expiresAt="2026-10-01T00:00:00Z", url="https://auth.example.test/consent",
                         idempotencyKey="auth-1")
    if path.endswith("/payments"):
        return 200, dict(payment="payment-1", status="pending", expiresAt="2026-10-01T00:00:00Z",
                         url="https://pay.example.test/checkout", idempotencyKey="pay-1")
    if path.endswith("/archive"):
        return 200, dict(thread="thread-1", archived=True)
    if path.endswith("/threads") and call["method"] == "GET":
        return 200, dict(threads=[], cursor=None)
    if path.endswith("/threads"):
        return 200, dict(thread="thread-1", message="message-1", status="accepted", cursor="thread-1:1",
                         idempotencyKey="start-1")
    return 200, snapshot()


@contextmanager
def fixture(responder=response):
    calls = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def handle_call(self):
            raw = self.rfile.read(int(self.headers.get("content-length", "0")))
            call = dict(path=self.path, method=self.command, headers=dict(self.headers),
                        body=json.loads(raw) if raw else None)
            calls.append(call)
            status, body = responder(call, len(calls))
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            if status == 429:
                self.send_header("Retry-After", "45")
            self.end_headers()
            self.wfile.write(json.dumps(body).encode())

        do_GET = do_POST = do_DELETE = handle_call

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/api", calls
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


class ThreadClientTest(unittest.TestCase):
    def test_sync_and_async_owner_input_preserve_business_arguments_without_uncertain_post_retry(self):
        from darwin_sdk.types.act_v3request_audience import ActV3RequestAudience
        from darwin_sdk.types.act_v3request_audience_message import ActV3RequestAudienceMessage_InputResponse

        request = ActV3RequestAudience(thread_id="original-thread", message=ActV3RequestAudienceMessage_InputResponse(
            request_id="pending-input", arguments={"text": "Original text", "confirm": True}))
        for asynchronous in (False, True):
            calls = []

            def respond(wire):
                calls.append(wire)
                return httpx.Response(503, json={"code": "UNKNOWN_AFTER_ACCEPTANCE"})

            if asynchronous:
                async def run():
                    async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as transport:
                        client = AsyncDarwin(api_key="fixture", httpx_client=transport, max_retries=3)
                        with self.assertRaises(ApiError):
                            await client.create_or_continue_act(request=request, idempotency_key="same-owner-response", request_options={"max_retries": 3})
                asyncio.run(run())
            else:
                with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
                    client = Darwin(api_key="fixture", httpx_client=transport, max_retries=3)
                    with self.assertRaises(ApiError):
                        client.create_or_continue_act(request=request, idempotency_key="same-owner-response", request_options={"max_retries": 3})
            self.assertEqual(len(calls), 1)
            self.assertEqual(calls[0].method, "POST")
            self.assertEqual(calls[0].url.path, "/api/v3/act")
            self.assertEqual(calls[0].headers["Idempotency-Key"], "same-owner-response")
            self.assertEqual(json.loads(calls[0].content), {"threadId": "original-thread", "message": {"type": "input_response", "requestId": "pending-input", "arguments": {"text": "Original text", "confirm": True}}})

    def test_legacy_navigator_list_keeps_thread_response_fields(self):
        state = dict(threads=[dict(threadId="asst_legacy", title="Research", archived=False,
                                  createdAt="2026-11-03T00:00:00Z", updatedAt="2026-11-03T00:00:00Z",
                                  role="administrator")], nextBefore=None)
        with fixture(lambda *_: (200, state)) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            page = client.list_navigator_threads()
            self.assertEqual(page.threads[0].thread_id, "asst_legacy")
            self.assertIsNone(page.next_before)
            self.assertEqual(calls[0]["path"], "/api/v3/threads")

    def test_canonical_thread_create_and_main_message_keep_the_same_thread(self):
        state = dict(conversationId="asst_parent", threadId="asst_parent", status="planning", goal="Research", messages=[], revisions=[], previousRuns=[], createdAt="2026-11-03T00:00:00Z", updatedAt="2026-11-03T00:00:00Z")
        with fixture(lambda *_: (200, state)) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            created = client.create_thread(client_request_id="00000000-0000-4000-8000-000000000001", title="Research")
            continued = client.post_thread_message("asst_parent", client_message_id="main-1", message="Find papers", target={"agentId": "research"})
            self.assertEqual(created.thread_id, continued.thread_id)
            self.assertEqual([call["path"] for call in calls], ["/api/v3/threads", "/api/v3/threads/asst_parent/messages"])
            self.assertEqual(calls[1]["body"]["clientMessageId"], "main-1")

    def test_ordinary_send_preserves_owner_attested_file_reference(self):
        with fixture() as (base_url, calls):
            client = Darwin(base_url=base_url, api_key="fixture-key", max_retries=0)
            body = SendMessageBody_Message(messageContent="Process this actual CSV", attachments=[{"type": "owner_file", "input": "ofi_original_bytes_ref"}], idempotencyKey="owner-file-message")
            client.send_message(thread="thread-1", request=body)
            self.assertEqual(len(calls), 1)
            self.assertEqual(calls[0]["path"], "/api/v2/act/threads/thread-1/messages")
            self.assertEqual(calls[0]["body"]["attachments"], [{"type": "owner_file", "input": "ofi_original_bytes_ref"}])

    def test_thread_states_and_partial_file_metadata_survive_without_another_submission(self):
        for status in ("queued", "running", "reconciling", "failed", "cancelled", "succeeded"):
            page = snapshot()
            page["actions"] = [dict(action="action", capability="operation", request="request", status=status,
                                   cancellationRequested=False)]
            artifact = dict(mediaType="application/pdf", fileName=None, sizeBytes=811, sha256="a" * 64)
            page["messages"] = [dict(type="result", message="result", **{"from": "agent"}, content=[],
                                     status="delivered" if status == "succeeded" else "unknown",
                                     createdAt="2026-11-02T00:00:00.000Z", data=dict(artifacts=[artifact]))]
            calls = []

            def respond(request):
                calls.append(request)
                return httpx.Response(200, json=page)

            with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
                value = Darwin(api_key="fixture", httpx_client=transport).get_act_thread("original")
                self.assertEqual(value.actions[0].status, status)
                self.assertEqual(value.messages[0].status, page["messages"][0]["status"])
                self.assertEqual(value.messages[0].data["artifacts"][0], artifact)
                self.assertEqual(len(calls), 1)
                self.assertEqual(calls[0].method, "GET")

    def test_artifact_ticket_preserves_arbitrary_mime_null_filename_and_integrity(self):
        for media_type in ("application/pdf", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "text/calendar"):
            artifact = dict(url="https://storage.example.test/opaque", expiresAt="2026-11-02T00:05:00.000Z",
                            disposition="attachment", mediaType=media_type, fileName=None, sizeBytes=811, sha256="a" * 64)
            calls = []

            def respond(request):
                calls.append(request)
                return httpx.Response(200, json=artifact)

            with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
                client = Darwin(api_key="fixture", httpx_client=transport)
                value = client.get_result_artifact_download_url("original", "opaque")
                self.assertEqual(value.media_type, media_type)
                self.assertIsNone(value.file_name)
                self.assertEqual(value.size_bytes, 811)
                self.assertEqual(value.sha256, "a" * 64)
                self.assertEqual(len(calls), 1)
                self.assertEqual(calls[0].method, "POST")  # Existing owner-authorized URL mint, not Act.

    def test_act_unknown_has_one_attempt_despite_client_and_request_retry_options(self):
        for outcome in ("server error", "lost reply", "malformed accepted reply"):
            for asynchronous in (False, True):
                with self.subTest(outcome=outcome, asynchronous=asynchronous):
                    calls = []

                    def respond(request):
                        calls.append(request)
                        if outcome == "lost reply":
                            raise httpx.RemoteProtocolError("reply lost after submission")
                        if outcome == "malformed accepted reply":
                            return httpx.Response(202, content=b"{")
                        return httpx.Response(503, json={"code": "UNKNOWN_AFTER_ACCEPTANCE"})

                    options = {"max_retries": 2, "additional_headers": {"X-Fixture": "kept"}}
                    request = dict(targets=[dict(agentId="agent_fixture")], message="Original intent")
                    if asynchronous:
                        async def run():
                            async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as transport:
                                client = AsyncDarwin(api_key="fixture", httpx_client=transport, max_retries=2)
                                with self.assertRaises(Exception):
                                    await client.create_or_continue_act(request=request, request_options=options)
                        asyncio.run(run())
                    else:
                        with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
                            client = Darwin(api_key="fixture", httpx_client=transport, max_retries=2)
                            with self.assertRaises(Exception):
                                client.create_or_continue_act(request=request, request_options=options)
                    self.assertEqual(len(calls), 1)
                    self.assertEqual(calls[0].method, "POST")
                    self.assertEqual(calls[0].headers["X-Fixture"], "kept")
                    self.assertEqual(options["max_retries"], 2)

    def test_act_request_read_keeps_sync_and_async_transient_retries(self):
        receipt = dict(type="request", actRequestId="original", searchId=None, status="pending",
                       createdAt="2026-11-02T00:00:00.000Z", threads=[dict(agentId="agent_fixture")])
        for asynchronous in (False, True):
            calls = []

            def respond(request):
                calls.append(request)
                self.assertEqual(request.method, "GET")
                return httpx.Response(503, json={"code": "temporary"}) if len(calls) == 1 else httpx.Response(200, json=receipt)

            if asynchronous:
                async def run():
                    async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as transport:
                        client = AsyncDarwin(api_key="fixture", httpx_client=transport, max_retries=1)
                        self.assertEqual((await client.get_act_request("original")).act_request_id, "original")
                with patch("darwin_sdk.core.http_client.asyncio.sleep", new=AsyncMock()):
                    asyncio.run(run())
            else:
                with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
                    client = Darwin(api_key="fixture", httpx_client=transport, max_retries=1)
                    with patch("darwin_sdk.core.http_client.time.sleep"):
                        self.assertEqual(client.get_act_request("original").act_request_id, "original")
            self.assertEqual(len(calls), 2)

    def test_act_accepted_is_a_handoff_receipt_not_provider_completion(self):
        receipt = dict(type="request", actRequestId="actreq_fixture", searchId=None,
                       status="completed", createdAt="2026-11-02T00:00:00.000Z",
                       threads=[dict(agentId="agent_fixture", threadId="thread_fixture")])
        with fixture(lambda *_: (202, receipt)) as (url, calls):
            value = Darwin(base_url=url, api_key="fixture-key").create_or_continue_act(
                request=dict(targets=[dict(agentId="agent_fixture")], message="Run this operation"))
            self.assertEqual(value.act_request_id, "actreq_fixture")
            self.assertEqual(value.threads[0].thread_id, "thread_fixture")
            self.assertIsNone(value.threads[0].state)
            self.assertEqual(len(calls), 1)

    def test_act_conflicts_keep_typed_recovery_without_automatic_post_retry(self):
        for code in ("ACT_ADMISSION_BLOCKED", "ACT_HANDOFF_UNCONFIRMED"):
            with self.subTest(code=code):
                failure = dict(
                    code=code, stage="admission" if code == "ACT_ADMISSION_BLOCKED" else "handoff",
                    retryable=False, message="Read the existing request.",
                    receipt=dict(type="request", actRequestId="actreq_fixture", searchId=None,
                                 status="failed", createdAt="2026-11-02T00:00:00.000Z",
                                 threads=[dict(agentId="agent_fixture", operationId="operation_fixture",
                                               operationRevision=4, errorCode="SOURCE_RECEIPT_MISSING")]),
                    blockers=[dict(agentId="agent_fixture", operationId="operation_fixture", operationRevision=4,
                                   code="SOURCE_RECEIPT_MISSING", nextAction=dict(
                                       type="reconcile_request", method="GET",
                                       path="/api/v3/act/requests/actreq_fixture"))])
                with fixture(lambda *_: (409, failure)) as (url, calls):
                    with self.assertRaises(ActConflictError) as error:
                        Darwin(base_url=url, api_key="fixture-key", max_retries=2).create_or_continue_act(
                            request=dict(targets=[dict(agentId="agent_fixture")], message="Run this operation"),
                            idempotency_key="original-attempt")
                    self.assertEqual(error.exception.status_code, 409)
                    self.assertEqual(error.exception.body.code, code)
                    self.assertFalse(error.exception.body.retryable)
                    self.assertEqual(error.exception.body.receipt.act_request_id, "actreq_fixture")
                    self.assertEqual(error.exception.body.blockers[0].operation_revision, 4)
                    self.assertEqual(len(calls), 1)
                    self.assertEqual(calls[0]["method"], "POST")
                    headers = {key.lower(): value for key, value in calls[0]["headers"].items()}
                    self.assertEqual(headers["idempotency-key"], "original-attempt")

    def test_async_act_conflict_preserves_typed_receipt_without_retry(self):
        failure = dict(code="ACT_HANDOFF_UNCONFIRMED", stage="handoff", retryable=False,
                       message="Read the existing request.",
                       receipt=dict(type="request", actRequestId="actreq_fixture", searchId=None,
                                    status="failed", createdAt="2026-11-02T00:00:00.000Z",
                                    threads=[dict(agentId="agent_fixture", errorCode="ACT_THREAD_START_FAILED")]),
                       blockers=[dict(agentId="agent_fixture", code="ACT_THREAD_START_FAILED",
                                      nextAction=dict(type="reconcile_request", method="GET",
                                                      path="/api/v3/act/requests/actreq_fixture"))])
        with fixture(lambda *_: (409, failure)) as (url, calls):
            async def run():
                with self.assertRaises(ActConflictError) as error:
                    await AsyncDarwin(base_url=url, api_key="fixture-key", max_retries=2).create_or_continue_act(
                        request=dict(targets=[dict(agentId="agent_fixture")], message="Run this operation"))
                self.assertEqual(error.exception.body.receipt.act_request_id, "actreq_fixture")
                self.assertFalse(error.exception.body.retryable)
            asyncio.run(run())
            self.assertEqual(len(calls), 1)

    def test_minimal_explicit_turns_and_unified_read(self):
        reply = dict(threadId="asst_fixture", conversationId="asst_fixture", status="planning",
                     messages=[], revisions=[], latestRevisionId=None, previousRuns=[],
                     createdAt="2026-11-01T00:00:00Z", updatedAt="2026-11-01T00:00:00Z",
                     goal="Find an agent", quote=None, funding=None, run=None,
                     conversation=dict(turns=[], nextBefore=None, eventCursor="0"))
        with fixture(lambda *_: (200, reply)) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            for method in ["live_search", "route", "execute"]:
                getattr(client, method)(message="Find an agent", client_message_id=method)
            client.read_thread("asst_fixture", assist_token="private-token", before="older")
            self.assertEqual([call["path"] for call in calls], [
                "/api/v3/live-search", "/api/v3/route", "/api/v3/execute",
                "/api/v3/threads/asst_fixture?before=older"])
            for call in calls[:3]:
                self.assertEqual(set(call["body"]), {"message", "clientMessageId"})
            headers = {key.lower(): value for key, value in calls[3]["headers"].items()}
            self.assertEqual(headers["x-assist-token"], "private-token")
            self.assertIsNone(calls[3]["body"])

    def test_navigate_guest_turn_and_private_recovery(self):
        reply = dict(conversationId="asst_fixture", conversationToken="fixture-private-token", status="planning",
                     messages=[], revisions=[], latestRevisionId=None, createdAt="2026-10-27T00:00:00Z",
                     updatedAt="2026-10-27T00:00:00Z", goal="Explain agent discovery.", previousRuns=[],
                     quote=None, funding=None, run=None,
                     conversation=dict(turns=[], nextBefore=None, eventCursor="0"))
        with fixture(lambda *_: (200, reply)) as (url, calls):
            client = Darwin(base_url=url, max_retries=0)
            body = dict(type="turn", clientMessageId="sdk-first", mode="chat",
                        message="Explain agent discovery.")
            result = client.navigate(type="turn", client_message_id=body["clientMessageId"], mode="chat", message=body["message"])
            client.get_navigate_request(result.conversation_id, assist_token=result.conversation_token, before="aturn_older")
            self.assertEqual(calls[0]["path"], "/api/v3/navigate")
            self.assertEqual(calls[0]["body"], body)
            self.assertEqual(calls[1]["path"], "/api/v3/navigate/conversations/asst_fixture?before=aturn_older")
            self.assertEqual(calls[1]["method"], "GET")
            headers = {key.lower(): value for key, value in calls[1]["headers"].items()}
            self.assertEqual(headers["x-assist-token"], "fixture-private-token")
            self.assertNotIn("authorization", headers)
            self.assertNotIn("x-api-key", headers)

    def test_adaptive_search_uses_v3(self):
        with fixture() as (base_url, calls):
            client = Darwin(base_url=base_url, api_key="fixture-key", max_retries=0)
            result = client.create_search(query="Find a tax agent")
            self.assertEqual(result.response.no_match_reason, "No eligible agent.")
            self.assertEqual(calls[0]["path"], "/api/v3/search")

    def test_payment_method_management_preserves_revision_body_and_safe_result(self):
        saved = dict(paymentMethodId="method-1", label="Test method", method="card",
                     status="active", isDefault=True, revision=4, expiresAt="2027-01-01T00:00:00Z")
        def respond(call, count):
            return 200, saved if count == 1 else dict(saved, status="revoked", isDefault=False, revision=5)
        with fixture(respond) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            selected = client.set_payment_method_default("acting", "method-1", expected_revision=3)
            self.assertEqual(selected.revision, 4)
            self.assertTrue(selected.is_default)
            revoked = client.revoke_payment_method("acting", "method-1", expected_revision=selected.revision)
            self.assertEqual(revoked.status, "revoked")
            self.assertFalse(revoked.is_default)
            self.assertEqual(revoked.revision, 5)
            self.assertEqual([(c["method"], c["path"], c["body"]) for c in calls], [
                ("POST", "/api/v2/account/ais/acting/payment-methods/method-1/default", dict(expectedRevision=3)),
                ("DELETE", "/api/v2/account/ais/acting/payment-methods/method-1", dict(expectedRevision=4)),
            ])
            self.assertTrue(all(c["headers"].get("x-api-key") == "fixture-key" for c in calls))

    def test_payment_method_conflict_does_not_retry_with_a_guessed_revision(self):
        with fixture(lambda *_: (409, dict(code="PAYMENT_METHOD_REVISION_CONFLICT"))) as (url, calls):
            with self.assertRaises(ApiError) as error:
                Darwin(base_url=url, api_key="fixture-key", max_retries=0).revoke_payment_method(
                    "acting", "method-1", expected_revision=3)
            self.assertEqual(error.exception.status_code, 409)
            self.assertEqual(error.exception.body.code, "PAYMENT_METHOD_REVISION_CONFLICT")
            self.assertEqual(len(calls), 1)
            self.assertEqual(calls[0]["body"], dict(expectedRevision=3))

    def test_async_payment_method_management_uses_the_same_contract(self):
        saved = dict(paymentMethodId="method-1", label="Test method", method="card",
                     status="active", isDefault=True, revision=1, expiresAt="2027-01-01T00:00:00Z")
        with fixture(lambda _call, count: (200, saved if count == 1 else dict(saved, status="revoked", isDefault=False, revision=2))) as (url, calls):
            async def run():
                client = AsyncDarwin(base_url=url, api_key="fixture-key", max_retries=0)
                selected = await client.set_payment_method_default("acting", "method-1", expected_revision=0)
                revoked = await client.revoke_payment_method("acting", "method-1", expected_revision=selected.revision)
                self.assertEqual(revoked.status, "revoked")
            asyncio.run(run())
            self.assertEqual([c["body"] for c in calls], [dict(expectedRevision=0), dict(expectedRevision=1)])

    def test_saved_payment_methods_are_an_ai_scoped_account_read(self):
        methods = [dict(paymentMethodId="method-1", label="Test method", method="card",
                        status="active", isDefault=True, revision=1, expiresAt="2027-01-01T00:00:00Z")]
        def respond(_call, count):
            return (200, dict(methods=[], nextCursor="method-0")) if count == 1 else \
                (200, dict(methods=methods, nextCursor=None))
        with fixture(respond) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            first = client.list_payment_methods("acting", limit=1)
            self.assertEqual(first.methods, [])
            self.assertEqual(first.next_cursor, "method-0")
            page = client.list_payment_methods("acting", limit=1, after_cursor=first.next_cursor)
            self.assertEqual(page.methods[0].payment_method_id, "method-1")
            self.assertEqual(page.methods[0].status, "active")
            self.assertIsNone(page.next_cursor)
            self.assertEqual(len(calls), 2)
            self.assertEqual(calls[0]["method"], "GET")
            self.assertEqual(parse_qs(urlsplit(calls[0]["path"]).query), dict(limit=["1"]))
            self.assertEqual(parse_qs(urlsplit(calls[1]["path"]).query),
                             dict(limit=["1"], afterCursor=["method-0"]))
            self.assertIsNone(calls[0]["body"])

    def test_target_account_management_wire_contract(self):
        def accounts_response(call, count):
            if count == 1:
                return 200, dict(accounts=[], nextCursor="grant-1")
            if count == 2:
                return 200, dict(accounts=[dict(
                    accountId="account-1", grantId="grant-2", targetAiId="target", label="Test account",
                    scopes=["read"], isDefault=True, retention="temporary", status="authentication_required",
                    retentionConsentedAt="2026-09-01T00:00:00Z", expiresAt=None, credentialExpiresAt=None,
                    canRefresh=False)],
                    nextCursor=None)
            if count == 3:
                return 200, dict(accountId="account-1", targetAiId="target", isDefault=True)
            return 200, dict(accountId="account-1", targetAiId="target", revoked=True)

        with fixture(accounts_response) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            first = client.list_target_accounts("acting", "target", limit=1, include_unavailable=False)
            self.assertEqual(first.accounts, [])
            self.assertEqual(first.next_cursor, "grant-1")
            self.assertEqual(parse_qs(urlsplit(calls[0]["path"]).query)["includeUnavailable"], ["false"])
            page = client.list_target_accounts("acting", "target", include_unavailable=True,
                                               limit=1, after_cursor=first.next_cursor)
            self.assertEqual(page.accounts[0].retention, "temporary")
            self.assertEqual(page.accounts[0].status, "authentication_required")
            self.assertEqual(str(page.accounts[0].retention_consented_at), "2026-09-01 00:00:00+00:00")
            self.assertFalse(page.accounts[0].can_refresh)
            self.assertTrue(client.set_target_account_default("acting", "target", "account-1").is_default)
            self.assertTrue(client.revoke_target_account("acting", "target", "account-1").revoked)
            self.assertEqual(parse_qs(urlsplit(calls[1]["path"]).query),
                             dict(includeUnavailable=["true"], limit=["1"], afterCursor=["grant-1"]))
            self.assertEqual([(call["method"], urlsplit(call["path"]).path) for call in calls], [
                ("GET", "/api/v2/account/ais/acting/connections/targets/target"),
                ("GET", "/api/v2/account/ais/acting/connections/targets/target"),
                ("POST", "/api/v2/account/ais/acting/connections/targets/target/account-1/default"),
                ("DELETE", "/api/v2/account/ais/acting/connections/targets/target/account-1"),
            ])
            self.assertTrue(all(call["headers"].get("x-api-key") == "fixture-key" for call in calls))

    def test_auth_credential_management_exposes_safe_metadata_and_explicit_revoke(self):
        credential = dict(credentialId="credential-1", provider="target-api", label="Work account",
                          status="ACTIVE", expiresAt=None, createdAt="2026-01-01T00:00:00Z",
                          revision="2026-01-01T00:00:00Z")
        def respond(_call, count):
            if count == 1:
                return 200, dict(credentials=[credential])
            return 200, dict(disconnected=True, revocationPending=False)

        with fixture(respond) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            listed = client.list_auth_credentials("acting")
            self.assertEqual(listed.credentials[0].credential_id, "credential-1")
            self.assertEqual(listed.credentials[0].label, "Work account")
            revoked = client.revoke_auth_credential("acting", "credential-1")
            self.assertTrue(revoked.disconnected)
            self.assertFalse(revoked.revocation_pending)
            self.assertEqual([(call["method"], call["path"], call["body"]) for call in calls], [
                ("GET", "/api/v2/account/ais/acting/connections/auth-credentials", None),
                ("DELETE", "/api/v2/account/ais/acting/connections/auth-credentials/credential-1", None),
            ])
            self.assertTrue(all(call["headers"].get("x-api-key") == "fixture-key" for call in calls))
            self.assertNotRegex(json.dumps(calls).lower(), r"token|secret|password|authorization")

    def test_account_vault_revocation_sends_oauth_and_conditional_revision(self):
        method = dict(paymentMethodId="method-1", label="Saved card", method="card",
                      status="revoked", isDefault=False, revision=5,
                      expiresAt="2027-01-01T00:00:00Z")
        def respond(_call, count):
            return 200, (dict(disconnected=True, revocationPending=True) if count == 1 else method)

        with fixture(respond) as (url, calls):
            client = Darwin(base_url=url, headers={"Authorization": "Bearer fixture-oauth"}, max_retries=0)
            revoked = client.revoke_account_auth_credential(
                "credential-1", if_match='"2026-01-01T00:00:00.000Z"')
            self.assertTrue(revoked.disconnected)
            self.assertTrue(revoked.revocation_pending)
            payment = client.revoke_account_payment_method("method-1", if_match='"4"')
            self.assertEqual(payment.status, "revoked")
            self.assertEqual([(call["method"], call["path"], call["headers"].get("If-Match")) for call in calls], [
                ("DELETE", "/api/v2/account/auth-credentials/credential-1", '"2026-01-01T00:00:00.000Z"'),
                ("DELETE", "/api/v2/account/payment-methods/method-1", '"4"'),
            ])
            self.assertTrue(all(call["headers"].get("Authorization") == "Bearer fixture-oauth" for call in calls))
            self.assertTrue(all("x-api-key" not in call["headers"] for call in calls))
            self.assertTrue(all(call["body"] is None for call in calls))

    def test_all_operations_and_typed_serialization(self):
        with fixture() as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            started = client.start_thread(request=StartThreadBody_Message(
                target_agent="target", message_content="Venue details?", agent="acting",
                idempotency_key="start-1"))
            self.assertEqual(started.thread, "thread-1")
            accepted = client.send_message("thread-1", request=SendMessageBody_Message(
                message_content="Which dates?", agent="acting", idempotency_key="message-1"))
            self.assertEqual(accepted.status, "accepted")
            page = client.get_thread("thread-1", agent="acting", cursor=accepted.cursor, wait=True)
            self.assertEqual(page.messages, [])
            self.assertFalse(page.has_more)
            listed = client.list_threads(agent="acting", target_agent="target", archived=False, needs_attention=True)
            self.assertIsNone(listed.cursor)
            archived = client.archive_thread("thread-1", agent="acting")
            self.assertTrue(archived.archived)
            auth = client.authenticate(request="auth-request-1", idempotency_key="auth-1")
            self.assertEqual(auth.status, "awaiting_consent")
            payment = client.pay(request="invoice-1", idempotency_key="pay-1")
            self.assertEqual(payment.status, "pending")
            self.assertFalse(hasattr(payment, "receipt_id"))
            self.assertTrue(hasattr(client, "archive_thread"))
            self.assertEqual([urlsplit(c["path"]).path for c in calls], [
                "/api/v2/act/threads", "/api/v2/act/threads/thread-1/messages", "/api/v2/act/threads/thread-1",
                "/api/v2/act/threads", "/api/v2/act/threads/thread-1/archive", "/api/v2/act/authentications",
                "/api/v2/act/payments"])
            self.assertEqual(calls[1]["body"], dict(messageType="message", messageContent="Which dates?",
                                                    agent="acting", idempotencyKey="message-1"))
            self.assertEqual(parse_qs(urlsplit(calls[2]["path"]).query)["wait"], ["true"])
            self.assertEqual(parse_qs(urlsplit(calls[3]["path"]).query)["archived"], ["false"])
            self.assertEqual(calls[4]["body"], dict(agent="acting"))
            self.assertTrue(all(c["headers"].get("x-api-key") == "fixture-key" for c in calls))

    def test_anonymous_search_and_explicit_credentials(self):
        with patch.dict(os.environ, {}, clear=True), fixture() as (url, calls):
            Darwin(base_url=url, api_key=None).search(
                query="venue", category="events", objective="seat 200 guests outdoors", num_results=5)
            Darwin(base_url=url, api_key="fixture-key").search(query="venue")
            Darwin(base_url=url, api_key=None, headers={"Authorization": "Bearer fixture-oauth"}).get_thread(
                "thread-1", agent="acting")
            self.assertNotIn("x-api-key", calls[0]["headers"])
            self.assertNotIn("Authorization", calls[0]["headers"])
            self.assertEqual(calls[0]["body"], dict(
                query="venue", category="events", objective="seat 200 guests outdoors", numResults=5))
            self.assertEqual(calls[1]["headers"]["x-api-key"], "fixture-key")
            self.assertEqual(calls[2]["headers"]["Authorization"], "Bearer fixture-oauth")

    def test_account_authorized_act_omits_legacy_agent_id(self):
        with fixture() as (url, calls):
            client = Darwin(base_url=url, headers={"Authorization": "Bearer fixture-oauth"})
            client.start_thread(
                request=StartThreadBody_Message(
                    target_agent="target",
                    message_content="Hello",
                    idempotency_key="account-start",
                )
            )
            client.get_thread("thread-1")
            self.assertNotIn("agent", calls[0]["body"])
            self.assertNotIn("agent", parse_qs(urlsplit(calls[1]["path"]).query))
            self.assertTrue(all(call["headers"]["Authorization"] == "Bearer fixture-oauth" for call in calls))

    def test_throttle_preserves_reason_and_retry_after(self):
        with fixture(lambda *_: (429, dict(error="act_reader_capacity_exceeded", retryAfterSeconds=45))) as (url, calls):
            with self.assertRaises(ApiError) as error:
                Darwin(base_url=url, api_key="fixture-key", max_retries=0).get_thread("thread-1", agent="acting")
            self.assertEqual(error.exception.status_code, 429)
            self.assertEqual(error.exception.body.retry_after_seconds, 45)
            self.assertEqual(len(calls), 1)

    def test_retry_keeps_message_identity(self):
        def respond(call, count):
            return (503, {"error": "unavailable"}) if count == 1 else response(call, count)
        with fixture(respond) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key", max_retries=0)
            args = dict(request=SendMessageBody_Message(
                message_content="Venue details?", agent="acting", idempotency_key="same-message"))
            with self.assertRaises(ApiError):
                client.send_message("thread-1", **args)
            result = client.send_message("thread-1", **args)
            self.assertEqual(result.status, "accepted")
            self.assertEqual(calls[0]["body"], calls[1]["body"])

    def test_async_receive_and_anonymous_search(self):
        with fixture() as (url, calls):
            async def run():
                client = AsyncDarwin(base_url=url, api_key=None, max_retries=0)
                await client.search(query="venue")
                page = await client.get_thread("thread-1", agent="acting", cursor="thread-1:0", wait=True,
                                               request_options={"additional_headers": {"Authorization": "Bearer fixture-oauth"}})
                self.assertEqual(page.cursor, "thread-1:0")
            asyncio.run(run())
            self.assertEqual(len(calls), 2)
            self.assertEqual(calls[1]["headers"]["Authorization"], "Bearer fixture-oauth")

    def test_payment_receipt_is_only_present_after_settlement(self):
        def respond(call, count):
            status, body = response(call, count)
            if count == 2:
                body.pop("url")
                body.update(status="settled", receipt="receipt-1")
            return status, body
        with fixture(respond) as (url, calls):
            client = Darwin(base_url=url, api_key="fixture-key")
            args = dict(request="invoice-1", idempotency_key="same-pay")
            pending = client.pay(**args)
            self.assertEqual(pending.status, "pending")
            self.assertFalse(hasattr(pending, "receipt"))
            settled = client.pay(**args)
            self.assertEqual(settled.status, "settled")
            self.assertEqual(settled.receipt, "receipt-1")
            self.assertEqual(calls[0]["body"], calls[1]["body"])

    def test_thread_id_cannot_inject_path_segments(self):
        with fixture() as (url, calls):
            Darwin(base_url=url, api_key="fixture-key").get_thread("thread/other", agent="acting")
            self.assertIn("/threads/thread%2Fother?", calls[0]["path"])


if __name__ == "__main__":
    unittest.main()

"""Generated Navigate clients retain reviewed Live controls over fake HTTP."""

import asyncio
import copy
import json
import unittest

import httpx
from darwin_sdk import AsyncDarwin, Darwin


class LiveSearchConsentTests(unittest.TestCase):
    """Exercise the actual generated sync/async serializer without providers."""

    def test_reviewed_controls_use_same_conversation_and_root_without_budget_fields(self):
        """Explicit revision replaces requirements while retaining owner routing."""
        for asynchronous in (False, True):
            with self.subTest(asynchronous=asynchronous):
                calls = []

                def respond(request):
                    calls.append((request.url.path, json.loads(request.content)))
                    return httpx.Response(200, json={
                        "conversationId": "asst_00000000-0000-0000-0000-000000000001",
                        "status": "planning", "goal": "Checksum public text",
                        "messages": [], "revisions": [], "latestRevisionId": None,
                        "previousRuns": [], "createdAt": "2030-01-01T00:00:00Z",
                        "updatedAt": "2030-01-01T00:00:00Z",
                    })

                control = {
                    "action": "start", "sourceTurnId": "choices",
                    "exactAgentIds": ["provider"], "shareableBrief": "Checksum public text hello",
                    "requirements": [{"requirementId": "sha", "statement": "Returns SHA256", "hard": True}],
                    "desiredMatches": 1,
                    "consent": "share_only_this_brief_with_read_only_free_operations",
                }
                revised = {**copy.deepcopy(control), "action": "revise", "sessionId": "lsctx:retained",
                           "requirements": [{"requirementId": "sha", "statement": "Returns MD5 instead", "hard": True}]}
                common = {"thread_id": "asst_00000000-0000-0000-0000-000000000001", "message": "Find a checksum service"}
                if asynchronous:
                    async def invoke():
                        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as http:
                            client = AsyncDarwin(api_key="fixture", base_url="https://fixture.invalid/api", httpx_client=http)
                            await client.navigate(**common, client_message_id="stable-start", live_search=control)
                            await client.navigate(**common, client_message_id="stable-revision", live_search=revised)
                    asyncio.run(invoke())
                else:
                    with httpx.Client(transport=httpx.MockTransport(respond)) as http:
                        client = Darwin(api_key="fixture", base_url="https://fixture.invalid/api", httpx_client=http)
                        client.navigate(**common, client_message_id="stable-start", live_search=control)
                        client.navigate(**common, client_message_id="stable-revision", live_search=revised)
                self.assertEqual(len(calls), 2)
                self.assertTrue(all(path == "/api/v3/navigate" for path, _ in calls))
                self.assertEqual(calls[0][1]["liveSearch"], control)
                self.assertEqual(calls[1][1]["liveSearch"], revised)
                self.assertEqual(calls[0][1]["threadId"], calls[1][1]["threadId"])
                self.assertTrue(all("budget" not in body and "ownerScope" not in body for _, body in calls))


if __name__ == "__main__":
    unittest.main()

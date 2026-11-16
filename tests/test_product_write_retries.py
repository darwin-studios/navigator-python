import unittest
import httpx
from darwin_sdk import Darwin, AsyncDarwin, RunTurnRequest

class ProductWriteRetries(unittest.TestCase):
    def test_sync_mutations_do_not_retry_even_when_requested(self):
        for name, failure in [(name, failure) for name in ['run','build','manage'] for failure in ['503','lost reply']]:
            calls = []
            def reply(request):
                calls.append(request)
                if failure == 'lost reply': raise httpx.ReadError('lost reply', request=request)
                return httpx.Response(503, json={'code':'UNAVAILABLE','message':'uncertain'})
            client = Darwin(api_key='fixture-only', max_retries=3, httpx_client=httpx.Client(transport=httpx.MockTransport(reply)))
            body = RunTurnRequest(type='turn', client_message_id='same-id', message='Review') if name == 'run' else {'action':'list_templates' if name == 'build' else 'list_agents'}
            with self.assertRaises(Exception):
                getattr(client,name)(request=body, idempotency_key='same-key', request_options={'max_retries':3})
            self.assertEqual(len(calls),1,(name,failure))

class AsyncProductWriteRetries(unittest.IsolatedAsyncioTestCase):
    async def test_async_mutations_do_not_retry_even_when_requested(self):
        for name, failure in [(name, failure) for name in ['run','build','manage'] for failure in ['503','lost reply']]:
            calls = []
            async def reply(request):
                calls.append(request)
                if failure == 'lost reply': raise httpx.ReadError('lost reply', request=request)
                return httpx.Response(503, json={'code':'UNAVAILABLE','message':'uncertain'})
            client = AsyncDarwin(api_key='fixture-only', max_retries=3, httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(reply)))
            body = RunTurnRequest(type='turn', client_message_id='same-id', message='Review') if name == 'run' else {'action':'list_templates' if name == 'build' else 'list_agents'}
            with self.assertRaises(Exception):
                await getattr(client,name)(request=body, idempotency_key='same-key', request_options={'max_retries':3})
            self.assertEqual(len(calls),1,(name,failure))

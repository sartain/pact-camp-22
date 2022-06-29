import atexit
import unittest

from pact import Consumer, Provider

pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
pact.start_service()
atexit.register(pact.stop_service)


class ToDoClientTest(unittest.TestCase):
    def test_get_todo_list(self):
        expected = {
            'id': "1",
            'list': ['Cheese']
        }

        (pact
         .given('Given an empty Todo list')
         .upon_receiving('When I add a Todo for Buy cheese')
         .with_request('get', '/todo/1')
         .will_respond_with(200, body=expected))
        pact.setup()
        result = item('1')
        pact.verify()
        self.assertEqual(result, expected)

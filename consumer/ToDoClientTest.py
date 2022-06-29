import atexit
import unittest

from pact import Consumer, Provider

pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
pact.start_service()
atexit.register(pact.stop_service)


class ToDoClientTest(unittest.TestCase):
  def can_create_to_do_list(self):
    expected = {
      'id': "1",
      'list': ['Cheese']
    }

    (pact
     .given('Given an empty Todo list')
     .upon_receiving('When I add a Todo for Buy cheese')
     .with_request('get', '/todo/1')
     .will_respond_with(200, body=expected))

    with pact:
      result = item('1')

    self.assertEqual(result, expected)

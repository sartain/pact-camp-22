import atexit
import unittest

from pact import Consumer, Provider


pact = Consumer('Consumer').has_pact_with(Provider('Provider'))
pact.start_service()
atexit.register(pact.stop_service)


class TodoContractTests(unittest.TestCase):
  def test_get_todo(self):
    expected = {
      'id': 123,
      'todo': ['Cheese']
    }

    (pact
     .given('Empty todo list')
     .upon_receiving('An order for cheese')
     .with_request('get', '/todo/123')
     .will_respond_with(200, body=expected))

    with pact:
      result = todo('123')

    self.assertEqual(result, expected)
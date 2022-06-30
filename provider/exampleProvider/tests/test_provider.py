"""pact test for user service provider"""

import logging

import unittest

from pact import Verifier

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# For the purposes of this example, the broker is started up as a fixture defined
# in conftest.py. For normal usage this would be self-hosted or using Pactflow.
PACT_BROKER_URL = "http://localhost"
PACT_BROKER_USERNAME = "pactbroker"
PACT_BROKER_PASSWORD = "pactbroker"

# For the purposes of this example, the Flask provider will be started up as part
# of run_pytest.sh when running the tests. Alternatives could be, for example
# running a Docker container with a database of test data configured.
# This is the "real" provider to verify against.
PROVIDER_HOST = "localhost"
PROVIDER_PORT = 5001
PROVIDER_URL = f"http://{PROVIDER_HOST}:{PROVIDER_PORT}"



class ProviderTest(unittest.TestCase):

    def test_user_service_provider_against_pact(self):

        verifier = Verifier(provider="Provider", provider_base_url=PROVIDER_URL)
        # Rather than requesting the Pact interactions from the Pact Broker, this
        # will perform the verification based on the Pact file locally.
        #
        # Because there is no way of knowing the previous state of an interaction,
        # if it has been successful in the past (since this is what the Pact Broker
        # is for), if the verification of an interaction fails then the success
        # result will be != 0, and so the test will FAIL.
        output, _ = verifier.verify_pacts(
            "../tests/consumer-provider.json",
            verbose=False,
        )
        assert output == 0

if __name__=="__main__":
    unittest.main()
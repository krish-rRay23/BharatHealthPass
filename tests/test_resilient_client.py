import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.core.resilient_client import ResilientGatewayClient

class TestResilientClient(unittest.TestCase):
    def test_succeeds_after_retry(self):
        call_count = [0]
        def flaky_call():
            call_count[0] += 1
            if call_count[0] < 2:
                raise ConnectionResetError("Transient network drop")
            return "SUCCESS"

        result = ResilientGatewayClient.execute_with_retry(flaky_call, max_retries=3)
        self.assertEqual(result, "SUCCESS")
        self.assertEqual(call_count[0], 2)

    def test_exhaustion_raises(self):
        def always_fails():
            raise TimeoutError("Gateway dead")

        with self.assertRaises(TimeoutError):
            ResilientGatewayClient.execute_with_retry(always_fails, max_retries=2)

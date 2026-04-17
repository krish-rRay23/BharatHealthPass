import unittest

def check_claim_spike(claims_last_30_days, threshold=4):
    return len(claims_last_30_days) >= threshold

class TestSpike(unittest.TestCase):
    def test_spike(self):
        self.assertTrue(check_claim_spike([1, 2, 3, 4]))
        self.assertFalse(check_claim_spike([1, 2]))

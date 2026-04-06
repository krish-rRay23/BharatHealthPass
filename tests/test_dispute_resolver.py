import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.fallback.dispute_resolver import DisputeResolver

class TestDisputeResolver(unittest.TestCase):
    def test_bpl_hardship(self):
        res = DisputeResolver.evaluate_hardship("BPL", 30000.0)
        self.assertTrue(res["eligible_for_hardship_grant"])
        self.assertEqual(res["grant_waiver_percent"], 0.50)

    def test_standard_tier(self):
        res = DisputeResolver.evaluate_hardship("GENERAL", 20000.0)
        self.assertFalse(res["eligible_for_hardship_grant"])
        self.assertEqual(res["residual_recovery_plan"], "STANDARD_30_DAY")

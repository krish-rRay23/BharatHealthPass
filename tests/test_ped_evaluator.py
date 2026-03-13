import unittest
from datetime import date
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.eligibility.ped_evaluator import PEDEvaluator

class TestPEDEvaluator(unittest.TestCase):
    def test_30_day_rejection(self):
        res = PEDEvaluator.evaluate(date(2026, 3, 1), date(2026, 3, 15), "FEVER", False)
        self.assertFalse(res["approved"])
        self.assertIn("30-day", res["reason"])

    def test_specific_ailment_waiting(self):
        res = PEDEvaluator.evaluate(date(2025, 6, 1), date(2026, 3, 15), "CATARACT", False)
        self.assertFalse(res["approved"])
        self.assertIn("CATARACT", res["reason"])

    def test_approved_after_waiting_period(self):
        res = PEDEvaluator.evaluate(date(2022, 1, 1), date(2026, 3, 15), "CATARACT", True)
        self.assertTrue(res["approved"])

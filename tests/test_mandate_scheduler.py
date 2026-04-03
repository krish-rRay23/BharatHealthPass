import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.fallback.mandate_scheduler import MandateScheduler

class TestMandateScheduler(unittest.TestCase):
    def test_schedule_generation(self):
        schedule = MandateScheduler.create_installment_schedule(10000.0, installments=3)
        self.assertEqual(len(schedule), 3)
        total = sum(item["amount"] for item in schedule)
        self.assertAlmostEqual(total, 10000.0, places=2)

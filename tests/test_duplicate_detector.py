import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.risk.duplicate_detector import DuplicateDetector

class TestDuplicateDetector(unittest.TestCase):
    def test_no_overlap(self):
        history = [{"hospital_id": "HOSP_A", "start_date": "2026-01-10", "end_date": "2026-01-15"}]
        res = DuplicateDetector.check_overlap(history, "2026-03-01", "2026-03-05")
        self.assertFalse(res["has_conflict"])

    def test_overlap_detected(self):
        history = [{"hospital_id": "HOSP_A", "start_date": "2026-03-02", "end_date": "2026-03-06"}]
        res = DuplicateDetector.check_overlap(history, "2026-03-04", "2026-03-08")
        self.assertTrue(res["has_conflict"])
        self.assertEqual(res["fraud_flag"], "OVERLAPPING_HOSPITALIZATION")

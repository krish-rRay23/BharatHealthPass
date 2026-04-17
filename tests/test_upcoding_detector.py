import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.risk.upcoding_detector import UpcodingDetector

class TestUpcodingDetector(unittest.TestCase):
    def test_justified_tier(self):
        res = UpcodingDetector.detect_mismatch("K35.8", 3)
        self.assertFalse(res["flagged_for_manual_medical_audit"])

    def test_blatant_upcoding(self):
        # A09 (simple diarrhea/gastroenteritis) billed as Tier 4 (major cardiac surgery)
        res = UpcodingDetector.detect_mismatch("A09", 4)
        self.assertTrue(res["flagged_for_manual_medical_audit"])
        self.assertEqual(res["risk_score_delta"], 0.45)

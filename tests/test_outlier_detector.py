import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.risk.outlier_detector import OutlierDetector

class TestOutlierDetector(unittest.TestCase):
    def test_normal_pricing(self):
        res = OutlierDetector.detect_outlier("APPENDICECTOMY", 48000.0)
        self.assertFalse(res["is_outlier"])
        self.assertEqual(res["severity"], "NORMAL")

    def test_inflated_pricing(self):
        # Mean 45000, std 8000. 75000 is z=3.75 -> critical
        res = OutlierDetector.detect_outlier("APPENDICECTOMY", 75000.0)
        self.assertTrue(res["is_outlier"])
        self.assertEqual(res["severity"], "CRITICAL_INFLATION")

import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.core.emergency_pass import EmergencyPassManager

class TestEmergencyPass(unittest.TestCase):
    def test_pass_lifecycle(self):
        token = EmergencyPassManager.issue_pass("P101", "12-3456-7890-1234", 100000.0, valid_hours=2)
        res = EmergencyPassManager.verify_pass(token)
        self.assertTrue(res["valid"])
        self.assertEqual(res["payload"]["sub"], "P101")
        self.assertEqual(res["payload"]["max_guarantee"], 100000.0)

    def test_corrupted_token(self):
        token = EmergencyPassManager.issue_pass("P101", "12-3456-7890-1234", 100000.0)
        corrupted = token[:-4] + "ABCD"
        res = EmergencyPassManager.verify_pass(corrupted)
        self.assertFalse(res["valid"])

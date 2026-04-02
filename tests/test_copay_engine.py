import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.claims.copay_engine import CopayEngine

class TestCopayEngine(unittest.TestCase):
    def test_bill_adjudication(self):
        items = [
            {"name": "Surgical Operation", "cost": 40000.0},
            {"name": "General Anesthesia", "cost": 10000.0},
            {"name": "PPE_Kit Deluxe", "cost": 2500.0},
            {"name": "Patient Diet Charge", "cost": 1500.0}
        ]
        res = CopayEngine.adjudicate_bill(items, copay_percentage=0.10)
        self.assertEqual(res["total_billed"], 54000.0)
        self.assertEqual(res["disallowed_non_payables"], 4000.0)
        self.assertEqual(res["insurer_payable"], 45000.0) # (50000 - 10%)
        self.assertEqual(res["total_patient_out_of_pocket"], 9000.0) # 5000 copay + 4000 disallowed

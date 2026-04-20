import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.settlement.voucher_generator import VoucherGenerator

class TestVoucherGenerator(unittest.TestCase):
    def test_voucher_generation(self):
        v = VoucherGenerator.generate_voucher("CASE_101", "HOSP_MAX", "TPA_MEDI_ASSIST", 85000.0)
        self.assertTrue(v["voucher_id"].startswith("VCH-"))
        self.assertTrue(v["utr_reference"].startswith("UTR-BHP-"))
        self.assertEqual(v["approved_amount"], 85000.0)
        self.assertEqual(v["status"], "GUARANTEED_RECONCILED")

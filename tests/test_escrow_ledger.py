import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.settlement.escrow_ledger import EscrowLedger

class TestEscrowLedger(unittest.TestCase):
    def test_double_entry_balance(self):
        ledger = EscrowLedger()
        ledger.post_transaction("TX1", "INSURER_POOL", "ESCROW_LOCK", 50000.0, "Pre-auth hold")
        ledger.post_transaction("TX2", "ESCROW_LOCK", "HOSPITAL_PAYABLE", 50000.0, "Discharge settlement")
        
        self.assertTrue(ledger.verify_invariant())
        self.assertEqual(ledger.get_balance("INSURER_POOL"), -50000.0)
        self.assertEqual(ledger.get_balance("ESCROW_LOCK"), 0.0)
        self.assertEqual(ledger.get_balance("HOSPITAL_PAYABLE"), 50000.0)

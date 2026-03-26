import unittest

def apply_dispute_lock(escrow_state, dispute_reason):
    if escrow_state["status"] == "LOCKED":
        escrow_state["status"] = "DISPUTE_HELD"
        escrow_state["dispute_reason"] = dispute_reason
        return True
    return False

class TestDispute(unittest.TestCase):
    def test_lock(self):
        state = {"status": "LOCKED", "amount": 50000.0}
        self.assertTrue(apply_dispute_lock(state, "Billing discrepancy"))
        self.assertEqual(state["status"], "DISPUTE_HELD")

import unittest

def restore_sum_insured(base_si, current_balance, claim_amount, auto_restore_feature=True):
    new_balance = current_balance - claim_amount
    restored = 0.0
    if new_balance <= 0 and auto_restore_feature:
        restored = base_si
        new_balance += base_si
    return {"balance": new_balance, "restored_amount": restored}

class TestRestoreSI(unittest.TestCase):
    def test_restore(self):
        res = restore_sum_insured(500000.0, 50000.0, 60000.0, auto_restore_feature=True)
        self.assertEqual(res["balance"], 490000.0)
        self.assertEqual(res["restored_amount"], 500000.0)

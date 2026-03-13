import unittest

TIER_DISCOUNTS = {"TIER_1_PREFERRED": 0.15, "TIER_2_NETWORK": 0.10, "NON_NETWORK": 0.0}

def calculate_discount(billed_amount, hospital_tier):
    rate = TIER_DISCOUNTS.get(hospital_tier, 0.0)
    discount = billed_amount * rate
    return {"discount": discount, "payable": billed_amount - discount}

class TestNetworkDiscount(unittest.TestCase):
    def test_tier_1(self):
        res = calculate_discount(100000.0, "TIER_1_PREFERRED")
        self.assertEqual(res["discount"], 15000.0)
        self.assertEqual(res["payable"], 85000.0)

import unittest

def calculate_netting(credits_list, debits_list):
    total_credit = sum(credits_list)
    total_debit = sum(debits_list)
    return total_credit - total_debit

class TestNetting(unittest.TestCase):
    def test_net(self):
        net = calculate_netting([50000, 25000], [40000, 15000])
        self.assertEqual(net, 20000)

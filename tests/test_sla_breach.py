import unittest

def check_sla_breach(elapsed_minutes, threshold_minutes=60):
    return elapsed_minutes > threshold_minutes

class TestSLABreach(unittest.TestCase):
    def test_breach(self):
        self.assertTrue(check_sla_breach(75))
        self.assertFalse(check_sla_breach(45))

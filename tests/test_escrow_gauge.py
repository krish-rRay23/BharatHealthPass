import unittest

class EscrowGauge:
    def __init__(self):
        self.active_count = 0
        self.locked_value = 0.0

    def inc(self, amt):
        self.active_count += 1
        self.locked_value += amt

    def dec(self, amt):
        self.active_count -= 1
        self.locked_value -= amt

class TestEscrowGauge(unittest.TestCase):
    def test_gauge(self):
        g = EscrowGauge()
        g.inc(50000.0)
        self.assertEqual(g.active_count, 1)
        self.assertEqual(g.locked_value, 50000.0)

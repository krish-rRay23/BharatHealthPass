import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.eligibility.room_rent_rule import RoomRentRule

class TestRoomRentRule(unittest.TestCase):
    def test_within_cap(self):
        # 5,00,000 SI -> 1% = 5,000/day
        res = RoomRentRule.calculate_room_eligibility(500000.0, "GENERAL", 4000.0, 3)
        self.assertEqual(res["admissible_amount"], 12000.0)
        self.assertEqual(res["patient_copay"], 0.0)
        self.assertEqual(res["proportionate_factor"], 1.0)

    def test_exceeding_cap(self):
        # 5,00,000 SI -> 1% = 5,000/day. Charged 7,500/day for 2 days
        res = RoomRentRule.calculate_room_eligibility(500000.0, "GENERAL", 7500.0, 2)
        self.assertEqual(res["admissible_amount"], 10000.0)
        self.assertEqual(res["patient_copay"], 5000.0)
        self.assertAlmostEqual(res["proportionate_factor"], 5000.0 / 7500.0, places=3)

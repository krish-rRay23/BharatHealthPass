import unittest

def parse_hfr_id(hfr_string):
    parts = hfr_string.strip().split("-")
    if len(parts) >= 2 and parts[0] == "IN":
        return {"country": parts[0], "state": parts[1], "facility_id": "-".join(parts[2:])}
    return None

class TestHFR(unittest.TestCase):
    def test_hfr(self):
        res = parse_hfr_id("IN-KA-HOSP-0012")
        self.assertIsNotNone(res)
        self.assertEqual(res["state"], "KA")

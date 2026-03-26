import unittest
from datetime import datetime, timezone, timedelta
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.settlement.hold_reversal import HoldReversalManager

class TestHoldReversal(unittest.TestCase):
    def test_active_hold(self):
        recent = (datetime.now(timezone.utc) - timedelta(hours=2)).isoformat()
        status = HoldReversalManager.evaluate_hold_status(recent, admitted=False)
        self.assertEqual(status, "ACTIVE_HOLD")

    def test_expired_reversal(self):
        old = (datetime.now(timezone.utc) - timedelta(hours=8)).isoformat()
        status = HoldReversalManager.evaluate_hold_status(old, admitted=False)
        self.assertEqual(status, "AUTO_REVERSED")

    def test_admitted_settled(self):
        recent = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        status = HoldReversalManager.evaluate_hold_status(recent, admitted=True)
        self.assertEqual(status, "SETTLED")

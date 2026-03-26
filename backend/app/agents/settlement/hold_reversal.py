"""Auto-Reversal of Unclaimed Hospital Reservation Holds."""
from datetime import datetime, timezone, timedelta

class HoldReversalManager:
    DEFAULT_HOLD_HOURS = 6

    @classmethod
    def evaluate_hold_status(cls, hold_time_iso: str, admitted: bool, hold_hours: int = DEFAULT_HOLD_HOURS) -> str:
        if admitted:
            return "SETTLED"
            
        hold_time = datetime.fromisoformat(hold_time_iso)
        if hold_time.tzinfo is None:
            hold_time = hold_time.replace(tzinfo=timezone.utc)
            
        now = datetime.now(timezone.utc)
        if now - hold_time > timedelta(hours=hold_hours):
            return "AUTO_REVERSED"
            
        return "ACTIVE_HOLD"

hold_reversal_mgr = HoldReversalManager()

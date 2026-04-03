"""Fallback UPI Autopay and e-NACH Mandate Scheduler."""
from datetime import datetime, timedelta, timezone

class MandateScheduler:
    @staticmethod
    def create_installment_schedule(total_amount: float, installments: int = 3) -> list:
        if installments <= 0:
            raise ValueError("Installments must be > 0")
            
        base_amount = round(total_amount / installments, 2)
        schedule = []
        now = datetime.now(timezone.utc)
        
        cumulative = 0.0
        for i in range(installments):
            due_date = (now + timedelta(days=30 * (i + 1))).strftime("%Y-%m-%d")
            # Adjust rounding in last installment
            amt = base_amount if i < installments - 1 else round(total_amount - cumulative, 2)
            cumulative += amt
            schedule.append({
                "installment_no": i + 1,
                "amount": amt,
                "due_date": due_date,
                "status": "SCHEDULED"
            })
        return schedule

mandate_scheduler = MandateScheduler()

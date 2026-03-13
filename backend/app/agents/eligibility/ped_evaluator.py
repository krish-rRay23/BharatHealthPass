"""Pre-Existing Disease (PED) and Waiting Period Evaluator."""
from datetime import date

SPECIFIC_WAITING_AILMENTS = {
    "CATARACT": 24, # 24 months
    "HERNIA": 24,
    "HYSTERECTOMY": 24,
    "KNEE_REPLACEMENT": 24
}

class PEDEvaluator:
    @staticmethod
    def evaluate(policy_inception_date: date, evaluation_date: date, ailment: str, is_ped: bool) -> dict:
        tenure_months = (evaluation_date.year - policy_inception_date.year) * 12 + (evaluation_date.month - policy_inception_date.month)
        
        # 1. 30-day initial waiting period check
        if (evaluation_date - policy_inception_date).days < 30:
            return {"approved": False, "reason": "Claimed within 30-day initial policy waiting period"}
        
        # 2. Specific ailment waiting period check
        ailment_key = ailment.upper()
        if ailment_key in SPECIFIC_WAITING_AILMENTS:
            required_months = SPECIFIC_WAITING_AILMENTS[ailment_key]
            if tenure_months < required_months:
                return {
                    "approved": False,
                    "reason": f"Waiting period of {required_months} months active for {ailment} (Elapsed: {tenure_months} months)"
                }

        # 3. Standard PED waiting period (typically 36 to 48 months, default 36)
        if is_ped and tenure_months < 36:
            return {
                "approved": False,
                "reason": f"Pre-existing disease 36-month waiting period active (Elapsed: {tenure_months} months)"
            }

        return {"approved": True, "reason": "Eligible under policy waiting period terms"}

ped_evaluator = PEDEvaluator()

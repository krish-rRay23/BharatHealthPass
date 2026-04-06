"""Dispute Escalation and Hardship Policy Handler."""

class DisputeResolver:
    @staticmethod
    def evaluate_hardship(patient_income_tier: str, dispute_amount: float) -> dict:
        # BPL (Below Poverty Line) / EWS (Economically Weaker Section)
        if patient_income_tier.upper() in ["BPL", "EWS"]:
            return {
                "eligible_for_hardship_grant": True,
                "grant_waiver_percent": 0.50,
                "residual_recovery_plan": "12_MONTH_ZERO_INTEREST",
                "interest_rate": 0.0
            }
        elif dispute_amount > 50000:
            return {
                "eligible_for_hardship_grant": False,
                "grant_waiver_percent": 0.0,
                "residual_recovery_plan": "6_MONTH_RESTRUCTURED",
                "interest_rate": 0.0
            }
        else:
            return {
                "eligible_for_hardship_grant": False,
                "grant_waiver_percent": 0.0,
                "residual_recovery_plan": "STANDARD_30_DAY",
                "interest_rate": 0.0
            }

dispute_resolver = DisputeResolver()

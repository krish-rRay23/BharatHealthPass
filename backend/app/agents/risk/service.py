import random

class RiskService:
    async def evaluate_risk(self, user_id: str, hospital_id: str, amount: float):
        """
        AI Model to predict risk of claim rejection or non-payment.
        Returns a 'Risk Score' (0.0 to 1.0). Lower is better.
        """
        # Feature: Amount Size
        risk = 0.1
        if amount > 100000:
            risk += 0.3
        
        # Feature: Hospital Credibility (Mock)
        if "TRUSTED" in hospital_id:
            risk -= 0.05
            
        # Random perturbation for AI realism
        risk += random.uniform(-0.05, 0.05)
        
        approved = risk < 0.4
        
        return {
            "risk_score": round(max(0, min(1, risk)), 2),
            "approved": approved,
            "max_approved_amount": amount if approved else amount * 0.5
        }

risk_agent = RiskService()

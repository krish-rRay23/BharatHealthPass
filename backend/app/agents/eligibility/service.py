from app.core.events import event_bus
from app.core.db import SessionLocal
from app.models.clinical import Policy
from sqlalchemy.future import select
import random

class EligibilityService:
    async def check_eligibility(self, user_id: str, treatment_type: str, estimated_cost: float):
        """
        Determines if the user is covered for the treatment.
        """
        async with SessionLocal() as session:
            # Mock: Fetch first policy
            result = await session.execute(select(Policy).where(Policy.user_id == user_id))
            policy = result.scalars().first()
            
            coverage_score = 0.0
            details = {}

            if not policy:
                # Mock: Create a default policy if none exists for demo
                policy = Policy(
                    user_id=user_id,
                    insurer_id="INS_001",
                    policy_number=f"POL_{user_id[:8]}",
                    coverage_limit=500000.0,
                    rules={"copay": 0}
                )
                session.add(policy)
                await session.commit()
            
            # Logic: Check limit
            if policy.coverage_limit >= estimated_cost:
                coverage_score = 0.95 # High confidence
                details = {"policy_id": policy.id, "limit": policy.coverage_limit}
            else:
                coverage_score = 0.4
                details = {"reason": "exceeds_limit"}

            return {
                "eligible": coverage_score > 0.8,
                "score": coverage_score,
                "details": details
            }

eligibility_agent = EligibilityService()

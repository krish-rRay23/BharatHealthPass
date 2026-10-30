from app.core.db import SessionLocal
from app.models.clinical import Claim
from app.core.events import event_bus
from sqlalchemy.future import select
import asyncio
import random

class ClaimsService:
    async def process_claim(self, case_id: str, policy_id: str, amount: float):
        """
        Submits claim packet to insurer (Stub).
        """
        async with SessionLocal() as session:
            claim = Claim(
                case_id=case_id,
                policy_id=policy_id,
                amount_claimed=amount,
                status="SUBMITTED"
            )
            session.add(claim)
            await session.commit()
            
            # Simulate Insurer Loop
            # In real system, this is async webhook Wait
            asyncio.create_task(self._simulate_insurer_response(case_id, claim.id))
            
            return claim

    async def _simulate_insurer_response(self, case_id: str, claim_id: str):
        await asyncio.sleep(5) # Simulate processing delay
        
        # Mock Logic: 80% Approval
        approved = random.random() < 0.8
        
        async with SessionLocal() as session:
            result = await session.execute(select(Claim).where(Claim.id == claim_id))
            claim = result.scalars().first()
            if claim:
                claim.status = "APPROVED" if approved else "REJECTED"
                claim.outcome_reason = "Policy limits met" if approved else "Documentation missing"
                await session.commit()
                
                event_type = "CLAIM_APPROVED" if approved else "CLAIM_REJECTED"
                await event_bus.publish(event_type, {
                    "case_id": case_id,
                    "claim_id": claim.id, 
                    "amount": claim.amount_claimed,
                    "reason": claim.outcome_reason
                })

claims_agent = ClaimsService()

from app.core.db import SessionLocal
from app.models.financial import Settlement
from app.core.events import event_bus
import uuid

class SettlementService:
    async def authorize_settlement(self, case_id: str, hospital_id: str, amount: float):
        """
        Locks the amount and issues an Auth Token for the hospital.
        """
        auth_token = f"AUTH_{uuid.uuid4().hex[:12].upper()}"
        
        async with SessionLocal() as session:
            settlement = Settlement(
                case_id=case_id,
                hospital_id=hospital_id,
                amount=amount,
                status="LOCKED",
                auth_token=auth_token
            )
            session.add(settlement)
            await session.commit()
            
            # Publish Event
            await event_bus.publish("SETTLEMENT_AUTHORIZED", {
                "case_id": case_id,
                "amount": amount,
                "auth_token": auth_token
            })
            
        return settlement

    async def retrieve_settlement(self, auth_token: str):
        # Hospital scans QR -> calls this
        pass

settlement_agent = SettlementService()

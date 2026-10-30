from app.core.events import event_bus
import logging

logger = logging.getLogger(__name__)

class FallbackService:
    async def execute_fallback(self, case_id: str, user_id: str, amount: float):
        """
        Triggers deduction from user's pre-authorized mandate/deposit.
        """
        # Logic: Call Payment Gateway Token (Stub)
        logger.warning(f"EXECUTING FALLBACK DEDUCTION for Case {case_id}: {amount} INR")
        
        # In real world, use Mandate ID linked to User
        success = True 
        
        if success:
            await event_bus.publish("FALLBACK_DEDUCTED", {
                "case_id": case_id,
                "user_id": user_id,
                "amount": amount,
                "status": "SUCCESS"
            })
            return True
        return False

fallback_agent = FallbackService()

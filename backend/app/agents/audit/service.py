from app.core.db import SessionLocal
from app.models.audit import AuditLog
from app.core.events import event_bus
from sqlalchemy.future import select
import logging
import json

logger = logging.getLogger(__name__)

class AuditService:
    def __init__(self):
        pass

    async def log_event(self, event_type: str, data: dict):
        """
        Persist event to Audit Log DB.
        """
        agent_name = data.get("source", "unknown")
        case_id = data.get("case_id")
        
        # Remove potentially redundant info if needed, but for audit we keep most.
        # Sensitive data masking should happen BEFORE publishing or be handled here.
        # For this system, we assume internal events are safe but we might mask specific keys if implemented.

        async with SessionLocal() as session:
            try:
                audit_entry = AuditLog(
                    event_type=event_type,
                    agent_name=agent_name,
                    case_id=case_id,
                    payload=data
                )
                session.add(audit_entry)
                await session.commit()
                logger.info(f"AUDIT LOGGED: {event_type} by {agent_name}")
            except Exception as e:
                logger.error(f"Failed to write to audit log: {e}")
                await session.rollback()

    async def start_listening(self):
        """
        Start consuming all events for auditing.
        """
        await event_bus.consume("audit_agent", self.log_event)

audit_agent = AuditService()

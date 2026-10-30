from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, JSON, DateTime
from datetime import datetime
from app.models.base import Base
import uuid

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    case_id: Mapped[str] = mapped_column(String, index=True, nullable=True) # Optional: link to a specific workflow case
    agent_name: Mapped[str] = mapped_column(String, nullable=False)
    event_type: Mapped[str] = mapped_column(String, index=True, nullable=False)
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)

    def __repr__(self):
        return f"<AuditLog(event={self.event_type}, agent={self.agent_name})>"

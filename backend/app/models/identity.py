from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, JSON, Boolean, ForeignKey
from app.models.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    mobile_hash: Mapped[str] = mapped_column(String, unique=True, index=True) # Hashed for privacy
    name: Mapped[str] = mapped_column(String) # Stored for demo, usually minimal
    # In real system, we'd have a vault ID or pointer, not raw PII mostly.
    
class ConsentArtefact(Base):
    __tablename__ = "consent_artefacts"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), index=True)
    purpose: Mapped[str] = mapped_column(String, nullable=False) # e.g. "TREATMENT_AUTH"
    scope: Mapped[JSON] = mapped_column(JSON, nullable=False) # e.g. ["INSURANCE_CHECK", "CREDIT_CHECK"]
    status: Mapped[str] = mapped_column(String, default="ACTIVE") # ACTIVE, REVOKED
    valid_until: Mapped[str] = mapped_column(String) # ISO Date
    signature: Mapped[str] = mapped_column(String) # Mock signature

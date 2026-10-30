from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, JSON, Float, ForeignKey
from app.models.base import Base
import uuid

class Policy(Base):
    __tablename__ = "policies"
    
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), index=True)
    insurer_id: Mapped[str] = mapped_column(String)
    policy_number: Mapped[str] = mapped_column(String)
    coverage_limit: Mapped[float] = mapped_column(Float)
    rules: Mapped[JSON] = mapped_column(JSON) # e.g. {"copay": 10, "excluded": ["COSMETIC"]}

class Claim(Base):
    __tablename__ = "claims"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    case_id: Mapped[str] = mapped_column(String, index=True)
    policy_id: Mapped[str] = mapped_column(String, ForeignKey("policies.id"))
    amount_claimed: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String, default="SUBMITTED") # SUBMITTED, APPROVED, REJECTED
    outcome_reason: Mapped[str] = mapped_column(String, nullable=True)

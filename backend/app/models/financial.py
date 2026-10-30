from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, ForeignKey, DateTime
from app.models.base import Base
import uuid

class Mandate(Base):
    __tablename__ = "mandates"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), index=True)
    amount_limit: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String, default="ACTIVE")
    bank_ref: Mapped[str] = mapped_column(String) # Mock UPI Mandate Ref

class Settlement(Base):
    __tablename__ = "settlements"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    case_id: Mapped[str] = mapped_column(String, index=True)
    hospital_id: Mapped[str] = mapped_column(String)
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String, default="PENDING") # PENDING, LOCKED, SETTLED, FAILED
    auth_token: Mapped[str] = mapped_column(String) # QR Token

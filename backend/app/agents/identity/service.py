from app.core.db import SessionLocal
from app.models.identity import User, ConsentArtefact
from app.core.events import event_bus
from sqlalchemy.future import select
import uuid
import hashlib

class IdentityService:
    async def get_or_create_user(self, mobile: str, name: str) -> User:
        # Mock OTP verification happened before this
        mobile_hash = hashlib.sha256(mobile.encode()).hexdigest()
        
        async with SessionLocal() as session:
            result = await session.execute(select(User).where(User.mobile_hash == mobile_hash))
            user = result.scalars().first()
            
            if not user:
                user = User(mobile_hash=mobile_hash, name=name)
                session.add(user)
                await session.commit()
                await session.refresh(user)
                
                # Emit User Created Event
                await event_bus.publish("USER_CREATED", {"user_id": user.id})
                
            return user

    async def create_consent(self, user_id: str, purpose: str, scope: list[str]) -> ConsentArtefact:
        # In real world, this involves signing a request
        artifact = ConsentArtefact(
            user_id=user_id,
            purpose=purpose,
            scope=scope,
            valid_until="2030-01-01T00:00:00Z", # Mock
            signature=f"SIGN_{uuid.uuid4()}" # Mock
        )
        
        async with SessionLocal() as session:
            session.add(artifact)
            await session.commit()
            await session.refresh(artifact)
            
            # Publish Event
            await event_bus.publish("CONSENT_GRANTED", {
                "consent_id": artifact.id, 
                "user_id": user_id,
                "scope": scope,
                "purpose": purpose
            })
            
        return artifact

    async def fetch_digilocker_kyc(self, user_id: str):
        # STUB: Mock external API call
        # Logic: We don't store this raw data long term, just return for processing
        return {
            "kyc_verified": True,
            "document_type": "AADHAAR",
            "assurance_level": "HIGH"
        }

identity_service = IdentityService()

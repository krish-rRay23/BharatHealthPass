from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.identity.service import identity_service

router = APIRouter()

class LoginRequest(BaseModel):
    mobile: str
    name: str

class ConsentRequest(BaseModel):
    user_id: str
    purpose: str
    scope: list[str] = ["INSURANCE", "CREDIT"]

@router.post("/login")
async def login(req: LoginRequest):
    # Mock OTP flow: assume verified
    user = await identity_service.get_or_create_user(req.mobile, req.name)
    return {"user_id": user.id, "token": "mock_session_token"}

@router.post("/consent")
async def grant_consent(req: ConsentRequest):
    artifact = await identity_service.create_consent(req.user_id, req.purpose, req.scope)
    return {"consent_id": artifact.id, "status": artifact.status}

@router.get("/kyc/{user_id}")
async def get_kyc(user_id: str):
    data = await identity_service.fetch_digilocker_kyc(user_id)
    return data

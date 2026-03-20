"""Offline Emergency Health Pass Generator and Authenticator."""
import base64
import json
import hmac
import hashlib
from datetime import datetime, timezone

SECRET = "bhp-offline-emergency-pass-key-2026"

class EmergencyPassManager:
    @staticmethod
    def issue_pass(patient_id: str, abha_id: str, max_guarantee: float, valid_hours: int = 12) -> str:
        header = {"alg": "HS256", "typ": "BHP-PASS"}
        issued_at = int(datetime.now(timezone.utc).timestamp())
        expires_at = issued_at + (valid_hours * 3600)
        
        payload = {
            "sub": patient_id,
            "abha": abha_id,
            "max_guarantee": max_guarantee,
            "iat": issued_at,
            "exp": expires_at,
            "nonce": hashlib.md5(f"{patient_id}-{issued_at}".encode()).hexdigest()[:8]
        }
        
        b64_header = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
        b64_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
        message = f"{b64_header}.{b64_payload}"
        sig = hmac.new(SECRET.encode(), message.encode(), hashlib.sha256).digest()
        b64_sig = base64.urlsafe_b64encode(sig).decode().rstrip("=")
        return f"{message}.{b64_sig}"

    @staticmethod
    def verify_pass(token: str) -> dict:
        parts = token.split(".")
        if len(parts) != 3:
            return {"valid": False, "error": "Malformed pass token"}
        
        message = f"{parts[0]}.{parts[1]}"
        expected_sig = base64.urlsafe_b64encode(hmac.new(SECRET.encode(), message.encode(), hashlib.sha256).digest()).decode().rstrip("=")
        if not hmac.compare_digest(parts[2], expected_sig):
            return {"valid": False, "error": "Signature mismatch"}
            
        payload = json.loads(base64.urlsafe_b64decode(parts[1] + "==").decode())
        if datetime.now(timezone.utc).timestamp() > payload["exp"]:
            return {"valid": False, "error": "Pass expired"}
            
        return {"valid": True, "payload": payload}

emergency_pass_mgr = EmergencyPassManager()

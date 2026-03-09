"""ABDM Cryptographic Consent Signer and Verifier."""
import hmac
import hashlib
import json
from datetime import datetime, timezone

SECRET_KEY = "bhp-abdm-consent-signing-secret"

class ConsentSigner:
    @staticmethod
    def generate_artefact(user_id: str, hip_id: str, hiu_id: str, purpose: str, expiry_iso: str) -> dict:
        artefact_payload = {
            "consentId": f"CONSENT-{user_id[:8]}-{int(datetime.now(timezone.utc).timestamp())}",
            "userId": user_id,
            "hipId": hip_id,
            "hiuId": hiu_id,
            "purpose": purpose,
            "expiry": expiry_iso,
            "status": "GRANTED"
        }
        serialized = json.dumps(artefact_payload, sort_keys=True)
        signature = hmac.new(SECRET_KEY.encode(), serialized.encode(), hashlib.sha256).hexdigest()
        artefact_payload["signature"] = signature
        return artefact_payload

    @staticmethod
    def verify_artefact(artefact: dict) -> bool:
        if "signature" not in artefact:
            return False
        signature = artefact["signature"]
        copy = dict(artefact)
        del copy["signature"]
        serialized = json.dumps(copy, sort_keys=True)
        expected = hmac.new(SECRET_KEY.encode(), serialized.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected):
            return False
        
        # Verify expiry
        expiry = datetime.fromisoformat(artefact["expiry"].replace("Z", "+00:00"))
        if datetime.now(timezone.utc) > expiry:
            return False
        return artefact.get("status") == "GRANTED"

consent_signer = ConsentSigner()

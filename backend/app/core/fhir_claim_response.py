"""ABDM FHIR ClaimResponse Resource Generator."""
import uuid
from datetime import datetime

class FHIRClaimResponseBuilder:
    @staticmethod
    def build(claim_id: str, patient_id: str, insurer_id: str, approved_amount: float) -> dict:
        return {
            "resourceType": "ClaimResponse",
            "id": str(uuid.uuid4()),
            "status": "active",
            "type": {
                "coding": [{"system": "http://terminology.hl7.org/CodeSystem/claim-type", "code": "institutional"}]
            },
            "use": "preauthorization",
            "patient": {"reference": f"Patient/{patient_id}"},
            "created": datetime.utcnow().isoformat() + "Z",
            "insurer": {"identifier": {"value": insurer_id}},
            "outcome": "complete",
            "total": [
                {
                    "category": {"coding": [{"code": "adjudicated"}]},
                    "amount": {"value": approved_amount, "currency": "INR"}
                }
            ]
        }

fhir_claim_response_builder = FHIRClaimResponseBuilder()

"""FHIR R4 Resource Builder for ABDM Integration."""
import uuid
from datetime import datetime

class FHIRBuilder:
    @staticmethod
    def build_patient_resource(user_id: str, abha_id: str, name: str, gender: str, birth_date: str) -> dict:
        return {
            "resourceType": "Patient",
            "id": user_id,
            "identifier": [
                {
                    "system": "https://healthid.ndhm.gov.in",
                    "value": abha_id
                }
            ],
            "name": [{"text": name}],
            "gender": gender.lower(),
            "birthDate": birth_date
        }

    @staticmethod
    def build_condition_resource(patient_id: str, icd_code: str, display_name: str) -> dict:
        return {
            "resourceType": "Condition",
            "id": str(uuid.uuid4()),
            "subject": {"reference": f"Patient/{patient_id}"},
            "code": {
                "coding": [
                    {
                        "system": "http://hl7.org/fhir/sid/icd-10",
                        "code": icd_code,
                        "display": display_name
                    }
                ]
            },
            "recordedDate": datetime.utcnow().isoformat() + "Z"
        }

fhir_builder = FHIRBuilder()

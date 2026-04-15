"""Hospital Desk Device Fingerprint and Staff Session Binding."""
import hashlib

class DeviceBindingValidator:
    @staticmethod
    def generate_fingerprint(device_id: str, hospital_id: str, app_salt: str = "bhp-desk-2026") -> str:
        raw = f"{device_id}:{hospital_id}:{app_salt}"
        return hashlib.sha256(raw.encode()).hexdigest()

    @staticmethod
    def validate_session(staff_role: str, active_fingerprint: str, registered_fingerprint: str) -> bool:
        if staff_role.upper() not in ["HOSPITAL_ADMIN", "RECEPTION_DESK", "TRIAGE_NURSE"]:
            return False
        return active_fingerprint == registered_fingerprint

device_binding_validator = DeviceBindingValidator()

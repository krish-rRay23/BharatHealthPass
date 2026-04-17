"""Upcoding Anomaly Detector."""

# Mapping common primary diagnoses to expected procedure complexity tiers
DIAGNOSIS_COMPLEXITY_TIERS = {
    "A09": 1,  # Infectious gastroenteritis (Tier 1: medical management)
    "J06": 1,  # Acute upper respiratory infection
    "K35": 3,  # Acute appendicitis (Tier 3: surgical appendectomy)
    "I21": 4   # Acute myocardial infarction (Tier 4: critical care / PTCA)
}

class UpcodingDetector:
    @staticmethod
    def detect_mismatch(icd_diagnosis: str, billed_tier: int) -> dict:
        base_code = icd_diagnosis.split(".")[0].upper()
        expected_tier = DIAGNOSIS_COMPLEXITY_TIERS.get(base_code, 2)
        
        # Anomaly if billed tier is 2 or more levels above diagnosis justification
        is_upcoding = billed_tier - expected_tier >= 2
        
        return {
            "diagnosis": icd_diagnosis,
            "expected_tier": expected_tier,
            "billed_tier": billed_tier,
            "flagged_for_manual_medical_audit": is_upcoding,
            "risk_score_delta": 0.45 if is_upcoding else 0.0
        }

upcoding_detector = UpcodingDetector()

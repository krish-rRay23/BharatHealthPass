"""Duplicate Admission and Overlapping Claims Detector."""
from datetime import datetime

class DuplicateDetector:
    @staticmethod
    def check_overlap(existing_admissions: list, new_admission_start: str, new_admission_end: str) -> dict:
        new_start = datetime.fromisoformat(new_admission_start)
        new_end = datetime.fromisoformat(new_admission_end)
        
        for adm in existing_admissions:
            curr_start = datetime.fromisoformat(adm["start_date"])
            curr_end = datetime.fromisoformat(adm["end_date"])
            
            # Check overlap: (StartA <= EndB) and (EndA >= StartB)
            if (new_start <= curr_end) and (new_end >= curr_start):
                return {
                    "has_conflict": True,
                    "conflicting_hospital": adm["hospital_id"],
                    "conflicting_dates": f"{adm['start_date']} to {adm['end_date']}",
                    "fraud_flag": "OVERLAPPING_HOSPITALIZATION"
                }
                
        return {"has_conflict": False, "fraud_flag": "NONE"}

duplicate_detector = DuplicateDetector()

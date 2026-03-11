"""Room Rent Capping and Proportionate Deduction Calculation."""

class RoomRentRule:
    NORMAL_ROOM_CAP_PERCENT = 0.01  # 1% of Sum Insured per day
    ICU_ROOM_CAP_PERCENT = 0.02     # 2% of Sum Insured per day

    @classmethod
    def calculate_room_eligibility(cls, sum_insured: float, room_type: str, charged_per_day: float, stay_days: int) -> dict:
        cap_percent = cls.ICU_ROOM_CAP_PERCENT if room_type.upper() == "ICU" else cls.NORMAL_ROOM_CAP_PERCENT
        max_allowed_per_day = sum_insured * cap_percent
        
        if charged_per_day <= max_allowed_per_day:
            return {
                "eligible": True,
                "admissible_amount": charged_per_day * stay_days,
                "patient_copay": 0.0,
                "proportionate_factor": 1.0
            }
        else:
            proportionate_factor = max_allowed_per_day / charged_per_day
            admissible = (max_allowed_per_day * stay_days)
            patient_copay = (charged_per_day - max_allowed_per_day) * stay_days
            return {
                "eligible": True,
                "admissible_amount": round(admissible, 2),
                "patient_copay": round(patient_copay, 2),
                "proportionate_factor": round(proportionate_factor, 4)
            }

room_rent_rule = RoomRentRule()

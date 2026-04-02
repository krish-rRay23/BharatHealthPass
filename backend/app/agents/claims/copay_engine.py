"""Itemized Hospital Bill Copay & Non-Payable Consumables Engine."""

NON_PAYABLE_KEYWORDS = {
    "GLOVES", "PPE_KIT", "THERMOMETER", "ADMISSION_FEE", "DIET_CHARGE", "ATTENDANT_PASS", "LUXURY_TAX"
}

class CopayEngine:
    @staticmethod
    def adjudicate_bill(items: list, copay_percentage: float = 0.10) -> dict:
        payable_sum = 0.0
        non_payable_sum = 0.0
        itemized_results = []
        
        for item in items:
            name = item["name"].upper().replace(" ", "_")
            cost = float(item["cost"])
            is_non_payable = any(k in name for k in NON_PAYABLE_KEYWORDS)
            
            if is_non_payable:
                non_payable_sum += cost
                itemized_results.append({"name": item["name"], "cost": cost, "status": "DISALLOWED", "reason": "Non-payable consumable item"})
            else:
                payable_sum += cost
                itemized_results.append({"name": item["name"], "cost": cost, "status": "APPROVED", "reason": "Standard medical expense"})
                
        patient_copay = payable_sum * copay_percentage
        insurer_share = payable_sum - patient_copay
        total_patient_liability = patient_copay + non_payable_sum
        
        return {
            "total_billed": payable_sum + non_payable_sum,
            "insurer_payable": round(insurer_share, 2),
            "patient_copay": round(patient_copay, 2),
            "disallowed_non_payables": round(non_payable_sum, 2),
            "total_patient_out_of_pocket": round(total_patient_liability, 2),
            "items": itemized_results
        }

copay_engine = CopayEngine()

"""Tripartite Settlement Voucher Generator."""
import uuid
import hashlib
from datetime import datetime

class VoucherGenerator:
    @staticmethod
    def generate_voucher(case_id: str, hospital_id: str, insurer_id: str, approved_amount: float) -> dict:
        voucher_id = f"VCH-{uuid.uuid4().hex[:10].upper()}"
        utr_ref = f"UTR-BHP-{hashlib.md5(voucher_id.encode()).hexdigest()[:12].upper()}"
        
        return {
            "voucher_id": voucher_id,
            "case_id": case_id,
            "hospital_id": hospital_id,
            "insurer_id": insurer_id,
            "approved_amount": approved_amount,
            "utr_reference": utr_ref,
            "settlement_rail": "IMPS_INSTANT_SETTLEMENT",
            "issued_timestamp": datetime.utcnow().isoformat() + "Z",
            "status": "GUARANTEED_RECONCILED"
        }

voucher_generator = VoucherGenerator()

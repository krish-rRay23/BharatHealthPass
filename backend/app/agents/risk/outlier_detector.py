"""Hospital Procedure Outlier and Inflation Detection."""
import statistics

REGIONAL_BENCHMARKS = {
    "ANGIOGRAPHY": {"mean": 25000.0, "std": 5000.0},
    "APPENDICECTOMY": {"mean": 45000.0, "std": 8000.0},
    "NORMAL_DELIVERY": {"mean": 35000.0, "std": 6000.0},
    "CESAREAN": {"mean": 60000.0, "std": 9000.0}
}

class OutlierDetector:
    @staticmethod
    def detect_outlier(procedure: str, billed_amount: float) -> dict:
        proc_key = procedure.upper()
        if proc_key not in REGIONAL_BENCHMARKS:
            return {"is_outlier": False, "z_score": 0.0, "recommendation": "Standard review"}
        
        bench = REGIONAL_BENCHMARKS[proc_key]
        z_score = (billed_amount - bench["mean"]) / bench["std"]
        
        is_outlier = z_score > 2.5 # > 2.5 standard deviations above average
        flag_critical = z_score > 3.5
        
        return {
            "procedure": procedure,
            "billed_amount": billed_amount,
            "benchmark_mean": bench["mean"],
            "z_score": round(z_score, 2),
            "is_outlier": is_outlier,
            "severity": "CRITICAL_INFLATION" if flag_critical else ("SUSPECT" if is_outlier else "NORMAL")
        }

outlier_detector = OutlierDetector()

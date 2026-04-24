"""Real-Time Health Pass Admission Metrics Collector."""

class MetricsCollector:
    def __init__(self):
        self.admission_latencies = []
        self.admissions_approved = 0
        self.admissions_rejected = 0

    def record_admission(self, latency_ms: float, approved: bool):
        self.admission_latencies.append(latency_ms)
        if approved:
            self.admissions_approved += 1
        else:
            self.admissions_rejected += 1

    def get_approval_rate(self) -> float:
        total = self.admissions_approved + self.admissions_rejected
        return round(self.admissions_approved / total, 4) if total > 0 else 0.0

    def get_p99_latency(self) -> float:
        if not self.admission_latencies:
            return 0.0
        sorted_lat = sorted(self.admission_latencies)
        idx = int(0.99 * len(sorted_lat))
        return sorted_lat[min(idx, len(sorted_lat) - 1)]

metrics_collector = MetricsCollector()

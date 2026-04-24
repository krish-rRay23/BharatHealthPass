import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.core.metrics_collector import MetricsCollector

class TestMetricsCollector(unittest.TestCase):
    def test_metrics_calculation(self):
        m = MetricsCollector()
        for i in range(100):
            m.record_admission(latency_ms=10.0 + i, approved=(i % 10 != 0))
            
        self.assertEqual(m.get_approval_rate(), 0.90)
        self.assertAlmostEqual(m.get_p99_latency(), 109.0, places=1)

import unittest
import asyncio
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.core.parallel_dispatcher import ParallelAdmissionDispatcher

class TestParallelDispatcher(unittest.TestCase):
    def test_successful_parallel_execution(self):
        async def mock_elig():
            await asyncio.sleep(0.01)
            return {"eligible": True}

        async def mock_risk():
            await asyncio.sleep(0.01)
            return {"approved": True, "score": 0.15}

        loop = asyncio.new_event_loop()
        res = loop.run_until_complete(ParallelAdmissionDispatcher.run_parallel_checks(mock_elig(), mock_risk()))
        loop.close()
        
        self.assertTrue(res["success"])
        self.assertTrue(res["eligibility"]["eligible"])
        self.assertTrue(res["risk"]["approved"])

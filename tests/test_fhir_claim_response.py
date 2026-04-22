import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.core.fhir_claim_response import FHIRClaimResponseBuilder

class TestFHIRClaimResponse(unittest.TestCase):
    def test_claim_response(self):
        resp = FHIRClaimResponseBuilder.build("CLM_001", "PAT_99", "INS_ICICI", 60000.0)
        self.assertEqual(resp["resourceType"], "ClaimResponse")
        self.assertEqual(resp["outcome"], "complete")
        self.assertEqual(resp["total"][0]["amount"]["value"], 60000.0)

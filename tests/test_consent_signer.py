import unittest
import sys
import os
from datetime import datetime, timedelta, timezone
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.identity.consent_signer import ConsentSigner

class TestConsentSigner(unittest.TestCase):
    def test_valid_consent(self):
        expiry = (datetime.now(timezone.utc) + timedelta(days=2)).isoformat()
        artefact = ConsentSigner.generate_artefact("usr_99", "HIP_01", "HIU_BHP", "TREATMENT_AUTH", expiry)
        self.assertTrue(ConsentSigner.verify_artefact(artefact))

    def test_tampered_consent(self):
        expiry = (datetime.now(timezone.utc) + timedelta(days=2)).isoformat()
        artefact = ConsentSigner.generate_artefact("usr_99", "HIP_01", "HIU_BHP", "TREATMENT_AUTH", expiry)
        artefact["purpose"] = "UNAUTHORIZED_ACCESS"
        self.assertFalse(ConsentSigner.verify_artefact(artefact))

    def test_expired_consent(self):
        expiry = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat()
        artefact = ConsentSigner.generate_artefact("usr_99", "HIP_01", "HIU_BHP", "TREATMENT_AUTH", expiry)
        self.assertFalse(ConsentSigner.verify_artefact(artefact))

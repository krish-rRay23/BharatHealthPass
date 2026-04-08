import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.audit.hash_chain import AuditHashChain

class TestAuditChain(unittest.TestCase):
    def test_chain_integrity(self):
        chain = AuditHashChain()
        chain.append_event("LOGIN", "user_1", {"ip": "127.0.0.1"})
        chain.append_event("TREATMENT_AUTH", "hosp_1", {"amount": 25000})
        self.assertTrue(chain.verify_chain())

    def test_tamper_detection(self):
        chain = AuditHashChain()
        chain.append_event("LOGIN", "user_1", {"ip": "127.0.0.1"})
        chain.append_event("TREATMENT_AUTH", "hosp_1", {"amount": 25000})
        # Tamper payload
        chain.chain[0]["payload"]["ip"] = "192.168.1.1"
        self.assertFalse(chain.verify_chain())

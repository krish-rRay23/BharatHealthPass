import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.core.fhir_builder import FHIRBuilder

class TestFHIRBuilder(unittest.TestCase):
    def test_patient_resource(self):
        p = FHIRBuilder.build_patient_resource("U123", "12-3456-7890-1234", "Rajesh Kumar", "male", "1988-04-12")
        self.assertEqual(p["resourceType"], "Patient")
        self.assertEqual(p["gender"], "male")
        self.assertEqual(p["identifier"][0]["value"], "12-3456-7890-1234")

    def test_condition_resource(self):
        c = FHIRBuilder.build_condition_resource("U123", "I21.9", "Acute myocardial infarction")
        self.assertEqual(c["resourceType"], "Condition")
        self.assertEqual(c["subject"]["reference"], "Patient/U123")
        self.assertEqual(c["code"]["coding"][0]["code"], "I21.9")

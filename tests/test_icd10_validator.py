import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.claims.icd10_validator import ICD10Validator

class TestICD10Validator(unittest.TestCase):
    def test_valid_codes(self):
        self.assertTrue(ICD10Validator.validate_code("I21.9"))
        self.assertTrue(ICD10Validator.validate_code("E11.9"))
        self.assertTrue(ICD10Validator.validate_code("J06"))

    def test_invalid_codes(self):
        self.assertFalse(ICD10Validator.validate_code("121.9"))
        self.assertFalse(ICD10Validator.validate_code("I2"))

    def test_category_lookup(self):
        self.assertEqual(ICD10Validator.get_category("I21.9"), "Diseases of the circulatory system")
        self.assertEqual(ICD10Validator.get_category("E11.9"), "Endocrine, nutritional and metabolic diseases")

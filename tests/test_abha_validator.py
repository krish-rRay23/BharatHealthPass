import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.identity.abha_validator import ABHAValidator

class TestABHAValidator(unittest.TestCase):
    def test_format_valid(self):
        self.assertTrue(ABHAValidator.validate_format("12-3456-7890-1234"))

    def test_format_invalid(self):
        self.assertFalse(ABHAValidator.validate_format("12345678901234"))
        self.assertFalse(ABHAValidator.validate_format("12-345-7890-1234"))

    def test_luhn_check(self):
        # 14 digits with valid Luhn
        # Calculate valid Luhn checksum for: 91-4523-8812-704
        # Let's verify known valid checksum
        digits = "9145238812704"
        # compute check digit
        total = 0
        for i, char in enumerate((digits + "0")[::-1]):
            n = int(char)
            if i % 2 == 1:
                n *= 2
                if n > 9: n -= 9
            total += n
        check_digit = (10 - (total % 10)) % 10
        valid_abha = f"91-4523-8812-704{check_digit}"
        self.assertTrue(ABHAValidator.is_valid_abha(valid_abha))

    def test_identical_digits_rejected(self):
        self.assertFalse(ABHAValidator.is_valid_abha("00-0000-0000-0000"))

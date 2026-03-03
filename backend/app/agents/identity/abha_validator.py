"""ABHA (Ayushman Bharat Health Account) Validator."""
import re

class ABHAValidator:
    @staticmethod
    def validate_format(abha_number: str) -> bool:
        """Validates 14-digit ABHA format: XX-XXXX-XXXX-XXXX."""
        pattern = r"^\d{2}-\d{4}-\d{4}-\d{4}$"
        return bool(re.match(pattern, abha_number))

    @staticmethod
    def validate_luhn(digits: str) -> bool:
        """Validates digits using Luhn algorithm."""
        clean_digits = digits.replace("-", "").strip()
        if not clean_digits.isdigit() or len(clean_digits) != 14:
            return False
        
        total = 0
        reverse_digits = clean_digits[::-1]
        for i, char in enumerate(reverse_digits):
            n = int(char)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    @classmethod
    def is_valid_abha(cls, abha_number: str) -> bool:
        if not cls.validate_format(abha_number):
            return False
        # Avoid all identical digits e.g. 11-1111-1111-1111
        cleaned = abha_number.replace("-", "")
        if len(set(cleaned)) == 1:
            return False
        return cls.validate_luhn(abha_number)

abha_validator = ABHAValidator()

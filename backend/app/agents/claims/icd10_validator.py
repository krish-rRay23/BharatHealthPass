"""ICD-10 Clinical Code Validator and Category Mapper."""
import re

ICD10_CATEGORIES = {
    "A": "Certain infectious and parasitic diseases",
    "B": "Certain infectious and parasitic diseases",
    "C": "Neoplasms",
    "D": "Diseases of the blood and blood-forming organs",
    "E": "Endocrine, nutritional and metabolic diseases",
    "I": "Diseases of the circulatory system",
    "J": "Diseases of the respiratory system",
    "K": "Diseases of the digestive system",
    "M": "Diseases of the musculoskeletal system",
    "O": "Pregnancy, childbirth and the puerperium",
    "S": "Injury, poisoning and certain consequences of external causes"
}

class ICD10Validator:
    @staticmethod
    def validate_code(code: str) -> bool:
        # Standard ICD-10 format: Letter followed by 2 digits, optionally dot and up to 4 alphanumeric
        pattern = r"^[A-Z][0-9]{2}(\.[0-9A-Z]{1,4})?$"
        return bool(re.match(pattern, code.strip()))

    @staticmethod
    def get_category(code: str) -> str:
        if not ICD10Validator.validate_code(code):
            return "UNKNOWN_INVALID"
        first_letter = code[0].upper()
        return ICD10_CATEGORIES.get(first_letter, "OTHER_CLASSIFIED")

icd10_validator = ICD10Validator()

import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))
from app.agents.identity.device_binding import DeviceBindingValidator

class TestDeviceBinding(unittest.TestCase):
    def test_valid_binding(self):
        fp = DeviceBindingValidator.generate_fingerprint("DEV_TAB_01", "HOSP_APOLLO")
        self.assertTrue(DeviceBindingValidator.validate_session("RECEPTION_DESK", fp, fp))

    def test_unauthorized_role(self):
        fp = DeviceBindingValidator.generate_fingerprint("DEV_TAB_01", "HOSP_APOLLO")
        self.assertFalse(DeviceBindingValidator.validate_session("UNVERIFIED_GUEST", fp, fp))

    def test_mismatched_device(self):
        fp1 = DeviceBindingValidator.generate_fingerprint("DEV_TAB_01", "HOSP_APOLLO")
        fp2 = DeviceBindingValidator.generate_fingerprint("DEV_TAB_02", "HOSP_APOLLO")
        self.assertFalse(DeviceBindingValidator.validate_session("RECEPTION_DESK", fp1, fp2))

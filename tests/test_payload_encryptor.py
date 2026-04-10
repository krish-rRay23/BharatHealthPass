import unittest
import base64

def xor_cipher(data_bytes, key_bytes):
    return bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data_bytes))

class TestCipher(unittest.TestCase):
    def test_symmetric(self):
        msg = b"Sensitive diagnosis record"
        key = b"secret-pass-2026"
        enc = xor_cipher(msg, key)
        dec = xor_cipher(enc, key)
        self.assertEqual(dec, msg)

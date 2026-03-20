import unittest

class RevocationCache:
    def __init__(self):
        self.revoked = set()

    def revoke(self, token_nonce):
        self.revoked.add(token_nonce)

    def is_revoked(self, token_nonce):
        return token_nonce in self.revoked

class TestRevocation(unittest.TestCase):
    def test_revocation(self):
        cache = RevocationCache()
        cache.revoke("nonce_99")
        self.assertTrue(cache.is_revoked("nonce_99"))
        self.assertFalse(cache.is_revoked("nonce_100"))

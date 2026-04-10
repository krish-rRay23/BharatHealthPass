import unittest
import random

def add_laplace_noise(val, epsilon=0.5, scale=1.0):
    # Mock laplace noise
    u = random.uniform(-1.0, 1.0)
    noise = (u * scale) / epsilon
    return val + noise

class TestDiffPrivacy(unittest.TestCase):
    def test_noise(self):
        noisy = add_laplace_noise(100.0)
        self.assertIsInstance(noisy, float)

import unittest

class MandateRetryQueue:
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts
        self.queue = {}

    def record_failure(self, mandate_id):
        curr = self.queue.get(mandate_id, 0) + 1
        self.queue[mandate_id] = curr
        return curr < self.max_attempts

class TestRetryQueue(unittest.TestCase):
    def test_retries(self):
        q = MandateRetryQueue(max_attempts=3)
        self.assertTrue(q.record_failure("M1"))
        self.assertTrue(q.record_failure("M1"))
        self.assertFalse(q.record_failure("M1"))

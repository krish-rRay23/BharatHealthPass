"""Resilient HTTP Client with Exponential Backoff and Jitter."""
import time
import random

class ResilientGatewayClient:
    @staticmethod
    def execute_with_retry(operation_fn, max_retries: int = 3, base_delay: float = 0.05):
        attempts = 0
        while True:
            try:
                return operation_fn()
            except Exception as e:
                attempts += 1
                if attempts >= max_retries:
                    raise e
                sleep_time = (base_delay * (2 ** attempts)) + random.uniform(0.01, 0.03)
                time.sleep(sleep_time)

resilient_client = ResilientGatewayClient()

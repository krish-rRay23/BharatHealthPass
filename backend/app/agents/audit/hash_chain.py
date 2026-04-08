"""Tamper-Evident SHA-256 Audit Log Hash Chain."""
import hashlib
import json

class AuditHashChain:
    def __init__(self):
        self.chain = []

    def append_event(self, event_type: str, actor_id: str, payload: dict) -> dict:
        prev_hash = self.chain[-1]["current_hash"] if self.chain else "GENESIS_ROOT_BHP_2026"
        
        block = {
            "index": len(self.chain),
            "prev_hash": prev_hash,
            "event_type": event_type,
            "actor_id": actor_id,
            "payload": payload
        }
        
        block_str = json.dumps(block, sort_keys=True)
        block["current_hash"] = hashlib.sha256(block_str.encode()).hexdigest()
        self.chain.append(block)
        return block

    def verify_chain(self) -> bool:
        for i, block in enumerate(self.chain):
            expected_prev = self.chain[i - 1]["current_hash"] if i > 0 else "GENESIS_ROOT_BHP_2026"
            if block["prev_hash"] != expected_prev:
                return False
                
            block_copy = dict(block)
            current_hash = block_copy.pop("current_hash")
            recomputed = hashlib.sha256(json.dumps(block_copy, sort_keys=True).encode()).hexdigest()
            if current_hash != recomputed:
                return False
        return True

audit_chain = AuditHashChain()

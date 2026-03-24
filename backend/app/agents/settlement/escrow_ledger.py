"""Double-Entry Escrow Ledger for Deferred Hospital Settlement."""
from datetime import datetime

class EscrowLedger:
    def __init__(self):
        self.entries = []
        self.balances = {}

    def post_transaction(self, tx_id: str, debit_account: str, credit_account: str, amount: float, description: str):
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        entry = {
            "tx_id": tx_id,
            "debit_account": debit_account,
            "credit_account": credit_account,
            "amount": amount,
            "description": description,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.entries.append(entry)
        
        self.balances[debit_account] = self.balances.get(debit_account, 0.0) - amount
        self.balances[credit_account] = self.balances.get(credit_account, 0.0) + amount
        return entry

    def get_balance(self, account: str) -> float:
        return self.balances.get(account, 0.0)

    def verify_invariant(self) -> bool:
        """In a double-entry ledger, sum of all balances must equal zero."""
        return abs(sum(self.balances.values())) < 1e-6

escrow_ledger = EscrowLedger()

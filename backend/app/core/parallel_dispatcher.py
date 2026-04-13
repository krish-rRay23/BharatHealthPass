"""Parallel Asynchronous Dispatcher for Multi-Agent Admission."""
import asyncio

class ParallelAdmissionDispatcher:
    @staticmethod
    async def run_parallel_checks(eligibility_coro, risk_coro, timeout_sec: float = 3.0):
        try:
            results = await asyncio.wait_for(
                asyncio.gather(eligibility_coro, risk_coro, return_exceptions=True),
                timeout=timeout_sec
            )
            elig_res, risk_res = results
            
            if isinstance(elig_res, Exception) or isinstance(risk_res, Exception):
                return {
                    "success": False,
                    "error": "One or more verification agents raised an exception",
                    "details": [str(r) for r in results if isinstance(r, Exception)]
                }
                
            return {
                "success": True,
                "eligibility": elig_res,
                "risk": risk_res
            }
        except asyncio.TimeoutError:
            return {"success": False, "error": "Agent evaluation timed out"}

dispatcher = ParallelAdmissionDispatcher()

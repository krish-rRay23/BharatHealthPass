from app.core.events import event_bus
from app.agents.eligibility.service import eligibility_agent
from app.agents.risk.service import risk_agent
from app.agents.settlement.service import settlement_agent
from app.agents.claims.service import claims_agent
from app.agents.fallback.service import fallback_agent

import logging
import uuid
import json

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self):
        # In-memory state tracking for demo. 
        # In prod, this would be Redis/DB backed with locking.
        self.active_cases = {} 

    async def start(self):
        await event_bus.consume("orchestrator", self.handle_event)
        
    async def handle_event(self, event_type: str, data: dict):
        logger.info(f"ORCHESTRATOR received: {event_type}")
        
        # 1. Start Case when User Consents to Treatment
        if event_type == "CONSENT_GRANTED" and data.get("purpose") == "TREATMENT_AUTH":
            user_id = data["user_id"]
            case_id = str(uuid.uuid4())
            self.active_cases[case_id] = {"state": "INIT", "user_id": user_id}
            
            # PARALLEL EXECUTION: Eligibility + Risk
            # Mock data for hospital/treatment context (would come from invite)
             # In a real flow, the 'Consent' is in response to a 'Hospital Request'
            hospital_id = "HOSP_APOLLO_01" 
            est_cost = 50000.0
            
            # Trigger Eligibility
            elig_result = await eligibility_agent.check_eligibility(user_id, "GENERAL_WARD", est_cost)
            
            # Trigger Risk
            risk_result = await risk_agent.evaluate_risk(user_id, hospital_id, est_cost)
            
            if elig_result["eligible"] and risk_result["approved"]:
                # Proceed to Settlement Auth
                await settlement_agent.authorize_settlement(case_id, hospital_id, est_cost)
            else:
                logger.error(f"Case {case_id} REJECTED due to Eligibility/Risk failure")

        # 2. Handle Claim Rejection -> Fallback
        elif event_type == "CLAIM_REJECTED":
            case_id = data.get("case_id")
            amount = data.get("amount")
            # Need to look up user_id from case state (omitted simplified)
            user_id = "USER_UNKNOWN_DEMO" 
            
            logger.info(f"Triggering Fallback for Case {case_id}")
            await fallback_agent.execute_fallback(case_id, user_id, amount)

orchestrator = Orchestrator()

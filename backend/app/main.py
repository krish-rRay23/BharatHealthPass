from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import asyncio
from app.core.config import settings
from app.core.db import engine, Base
from app.core.events import event_bus

# Import models to ensure they are registered with Base
from app.models.audit import AuditLog
from app.models.identity import User, ConsentArtefact
from app.models.financial import Mandate, Settlement
from app.models.clinical import Policy, Claim
from app.agents.audit.service import audit_agent

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting BHP System...")
    
    # 1. DB Init
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # 2. Redis Check
    try:
        await event_bus.redis.ping()
        print("Connected to Redis Event Bus")
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")

    # 3. Start Background Agents (Audit + Orchestrator)
    audit_task = asyncio.create_task(audit_agent.start_listening())
    
    from app.core.orchestrator import orchestrator
    orch_task = asyncio.create_task(orchestrator.start())
    
    yield
    
    # Shutdown
    audit_task.cancel()
    orch_task.cancel()
    await event_bus.redis.close()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, set to specific frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api import identity

app.include_router(identity.router, prefix="/api/v1/identity", tags=["Identity"])


@app.get("/health")
async def health():
    return {"status": "ok"}

from fastapi import FastAPI
from app.routers import contact
from app import models
from app.database import init_db
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.middleware.rate_limit import RateLimitMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    # Cleanup code can go here if needed

app = FastAPI(lifespan=lifespan)

app.add_middleware(RateLimitMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(contact.router)

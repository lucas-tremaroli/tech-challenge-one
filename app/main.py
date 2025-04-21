from fastapi import FastAPI, Depends
from app.core.auth import validate_api_key
from app.api.endpoints import production

app = FastAPI(
    title="FastAPI",
    description="A FastAPI application",
    version="0.1.0",
)

app.include_router(production.router)

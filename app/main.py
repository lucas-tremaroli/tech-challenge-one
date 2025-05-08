from fastapi import FastAPI
from app.api.endpoints import (
    production,
    auth
)

app = FastAPI(
    title="FastAPI",
    description="A FastAPI application",
    version="0.1.0",
)

app.include_router(production.router)
app.include_router(auth.router)

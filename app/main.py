import logging
from fastapi import FastAPI
from app.core.config import get_settings
from app.api.v1 import embrapa, auth

logging.getLogger('passlib').setLevel(logging.ERROR)

settings = get_settings()

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    summary=settings.summary,
    contact=settings.contact,
)

app.include_router(auth.router)
app.include_router(embrapa.router)

@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to my first Tech Challenge."
    }

@app.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint.
    """
    return {
        "status": "ok"
    }

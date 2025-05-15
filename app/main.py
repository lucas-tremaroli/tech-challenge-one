from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import (
    embrapa,
    auth
)

app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    summary=settings.summary,
    contact=settings.contact,
)

app.include_router(auth.router)
app.include_router(embrapa.router)

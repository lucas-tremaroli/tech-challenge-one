from fastapi import APIRouter, Depends
from app.core.auth import validate_api_key

router = APIRouter(
    prefix="/production",
    tags=["production"],
)


@router.get("/")
async def ping(
        api_key: str = Depends(validate_api_key)
):
    return {"ping": "pong"}

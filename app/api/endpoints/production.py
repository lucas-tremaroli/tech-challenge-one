from fastapi import APIRouter, Depends
from app.core.auth import validate_api_key
from app.services.production_service import ProductionService

ps = ProductionService()

router = APIRouter(
    prefix="/production",
    tags=["production"],
)


@router.get("/")
async def ping(
        api_key: str = Depends(validate_api_key)
):
    table = ps.get_production_data(year=2023)
    data = ps.parse(table)
    return data

from fastapi import APIRouter
from app.services.production_service import ProductionService

ps = ProductionService()

router = APIRouter(
    prefix="/production",
    tags=["production"],
)


@router.get("/")
async def ping():
    table = ps.get_production_data(year=2023)
    data = ps.parse(table)
    return data

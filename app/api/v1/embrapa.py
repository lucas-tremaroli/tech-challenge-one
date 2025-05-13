from fastapi import APIRouter
from app.services.extraction_service import ExtractionService

es = ExtractionService()

router = APIRouter(
    prefix="/embrapa",
    tags=["embrapa"],
)


@router.get("/")
async def ping():
    data = es.get_production_data(year=2023)
    return data

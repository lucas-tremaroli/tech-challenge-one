from typing import Annotated
from fastapi import APIRouter, Depends
from app.services.extraction_service import ExtractionService
from app.core.auth import (
    User,
    get_current_active_user
)

es = ExtractionService()

router = APIRouter(
    prefix="/embrapa",
    tags=["embrapa"],
)


@router.get("/production/{year}")
async def production(
    year: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    This endpoint gets the production data for the given year.
    """
    data = es.get_production_data(year)
    return data

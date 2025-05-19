from typing import Annotated
from fastapi import APIRouter, Depends
from app.services.production_service import ProductionService
from app.services.processing_service import ProcessingService
from app.services.commercial_service import CommercialService
from app.core.auth import (
    User,
    get_current_active_user
)

production_service = ProductionService()
processing_service = ProcessingService()
commercial_service = CommercialService()

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
    data = production_service.get_production_data(year)
    return data


@router.get("/processing/{year}/{option}")
async def processing(
    year: int,
    option: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    This endpoint gets the processing data for the given year and option.
    """
    data = processing_service.get_processing_data(year, option)
    return data


@router.get("/commercial/{year}")
async def commercial(
    year: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    This endpoint gets the commercial data for the given year.
    """
    data = commercial_service.get_commercial_data(year)
    return data

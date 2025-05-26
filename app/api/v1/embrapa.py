from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from app.services.url_service import UrlService
from app.services.scrap_service import ScrapService
from app.core.auth import User, get_current_active_user
from app.schemas.endpoints import EndpointEnum, ConnectionError

url_service = UrlService()
scrap_service = ScrapService()

router = APIRouter(
    prefix="/embrapa",
    tags=["Scrapping"],
)


@router.get(
    "/production/{year}",
    responses={500: {"model": ConnectionError}}
)
async def production(
    year: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    This endpoint gets the production data for the given year.
    """
    url = url_service.parse_url(
        EndpointEnum.production,
        year
    )
    data = scrap_service.get_data(url)
    if isinstance(data, Exception):
        raise HTTPException(
            status_code=500,
            detail=str(data)
        )
    return data


@router.get(
    "/processing/{year}/{option}",
    responses={500: {"model": ConnectionError}}
)
async def processing(
    year: int,
    option: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    This endpoint gets the processing data for the given year and option.
    """
    url = url_service.parse_url(
        EndpointEnum.processing,
        year,
        option
    )
    data = scrap_service.get_data(url)
    if isinstance(data, Exception):
        raise HTTPException(
            status_code=500,
            detail=str(data)
        )
    return data


@router.get(
    "/commercial/{year}",
    responses={500: {"model": ConnectionError}}
)
async def commercial(
    year: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    This endpoint gets the commercial data for the given year.
    """
    url = url_service.parse_url(
        EndpointEnum.commercial,
        year
    )
    data = scrap_service.get_data(url)
    if isinstance(data, Exception):
        raise HTTPException(
            status_code=500,
            detail=str(data)
        )
    return data


@router.get(
    "/import/{year}/{option}",
    responses={500: {"model": ConnectionError}}
)
async def importation(
    year: int,
    option: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    This endpoint gets the export data for the given year.
    """
    url = url_service.parse_url(
        EndpointEnum.importation,
        year,
        option
    )
    data = scrap_service.get_data(url)
    if isinstance(data, Exception):
        raise HTTPException(
            status_code=500,
            detail=str(data)
        )
    return data

@router.get(
    "/export/{year}/{option}",
    responses={500: {"model": ConnectionError}}
)
async def exportation(
    year: int,
    option: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    This endpoint gets the export data for the given year.
    """
    url = url_service.parse_url(
        EndpointEnum.exportation,
        year,
        option
    )
    data = scrap_service.get_data(url)
    if isinstance(data, Exception):
        raise HTTPException(
            status_code=500,
            detail=str(data)
        )
    return data

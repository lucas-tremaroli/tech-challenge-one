from fastapi import APIRouter, Depends
from app.core.auth import validate_api_key
from app.services.production_service import get_production_data

router = APIRouter(
    prefix="/production",
    tags=["production"],
)


@router.get("/")
async def ping(
        api_key: str = Depends(validate_api_key)
):
    table = get_production_data(2023)
    target_rows = table.select('tr:has(td.tb_subitem:nth-child(1))'
                              ':has(td.tb_subitem:nth-child(2))')
    data = {}
    for row in target_rows:
        cells = row.find_all('td', class_='tb_subitem')
        if len(cells) == 2:
            product = cells[0].text.strip()
            quantity = cells[1].text.strip()
            data[product] = quantity
    return data

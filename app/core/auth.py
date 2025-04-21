from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status

API_KEY_NAME = "X-API-Key"
API_KEYS = [
    "my_api_key",
]

api_key_header = APIKeyHeader(name=API_KEY_NAME)


async def validate_api_key(
        api_key: str | None = Security(api_key_header),
):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    elif api_key not in API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    else:
        return api_key

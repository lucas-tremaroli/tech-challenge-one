from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


markdown_description = """

### Description

This API provides authenticated access to production, processing, and commercial data related to grape and wine-growing, sourced from Embrapa's website. It's designed to serve clean, structured JSON data for machine learning models, dashboards, and notebooks.

### Authentication

To access protected endpoints, you first need to authenticate.

1.  Click 'Authorize' and enter the following credentials:

    -   **Username**: `fiap`
    -   **Password**: `secret`

3.  Once authorized, you can access all protected data endpoints by clicking on 'Try it out'.
"""

class Settings(BaseSettings):
    title: str = "Vitiviniculture Data API"
    description: str = markdown_description
    version: str = "0.1.0"
    summary: str = "A RESTful API for vitiviniculture data retrieval and analysis, developed as the first tech challenge for FIAP's ML course."
    contact: dict = {
        "name": "GitHub project",
        "url": "https://github.com/lucas-tremaroli/tech-challenge-one",
    }

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


markdown_description = """
## Authentication

Click on **Authorize** and use the following credentials:

- **User**: fiap
- **Password**: secret
"""

class Settings(BaseSettings):
    title: str = "Tech Challange API"
    description: str = markdown_description
    version: str = "0.1.0"
    summary: str = "This is a FastAPI project for the phase one tech challenge."
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

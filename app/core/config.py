from pydantic_settings import BaseSettings


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
    redis_host: str = "redis"
    redis_port: int = 6379

settings = Settings()

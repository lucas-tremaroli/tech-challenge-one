from fastapi import FastAPI, Depends
from app.core.auth import validate_api_key

app = FastAPI(
    title="FastAPI",
    description="A FastAPI application",
    version="0.1.0",
)


@app.get("/")
async def root(api_key: str = Depends(validate_api_key)):
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

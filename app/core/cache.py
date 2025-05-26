import redis
from redis.typing import ResponseT
from app.core.config import settings

class Cache:
    def __init__(self):
        self.host = settings.redis_host
        self.port = settings.redis_port
        self.client = redis.Redis(host=self.host, port=self.port, decode_responses=True)

    def set(self, key: str, value: str) -> None:
        self.client.set(key, value)

    def get(self, key: str) -> ResponseT:
        return self.client.get(key)

    def delete(self, key: str) -> None:
        self.client.delete(key)

    def fallback(self, key: str) -> ResponseT:
        return self.get(key) if self.client.exists(key) else None

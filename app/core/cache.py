import json
import redis
from redis.typing import ResponseT
from app.core.config import get_settings
from posix import replace

settings = get_settings()

class Cache:
    def __init__(self):
        self.host = settings.REDIS_HOST
        self.port = settings.REDIS_PORT
        self.client = redis.Redis(host=self.host, port=self.port, decode_responses=True)

    def set(self, key: str, value: str) -> None:
        self.client.set(key, value)

    def get(self, key: str) -> ResponseT:
        return self.client.get(key)

    def delete(self, key: str) -> None:
        self.client.delete(key)

    def fallback(self, key: str) -> ResponseT:
        if self.client.exists(key):
            data = self.get(key)
            data = str(data).replace("'", '"')
            json_data = json.loads(data)
            return json_data
        else:
            return None

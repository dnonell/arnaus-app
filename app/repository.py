from functools import lru_cache
from typing import Any, Optional

from app.settings import get_settings
from redis import Redis


@lru_cache(1)
def _connect() -> Redis:
    settings = get_settings()
    redis = Redis.from_url(url=str(settings.redis_dsn), decode_responses=True)
    return redis


def health_check() -> bool:
    redis = _connect()
    return redis.ping() == "PONG"


def get_value(name: str) -> Optional[Any]:
    redis = _connect()
    return redis.get(name=name)


def set_value(name: str, value: str) -> bool:
    redis = _connect()
    redis.set(name=name, value=value)
    return True

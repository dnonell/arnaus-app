from functools import lru_cache

from app import constants
from pydantic import Field, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redis_dsn: RedisDsn = Field(default=constants.DEFAULT_REDIS_DNS)


@lru_cache(1)
def get_settings() -> Settings:
    return Settings()

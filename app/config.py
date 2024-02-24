import os
from functools import lru_cache
from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import Field


os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = "1"


class Settings(BaseSettings):
    ASTRADB_KEYSPACE: str = os.environ.get('ASTRADB_KEYSPACE')
    ASTRADB_CLIENT_ID: str = os.environ.get('ASTRADB_CLIENT_ID')
    ASTRADB_CLIENT_SECRET: str = os.environ.get('ASTRADB_CLIENT_SECRET')

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()

from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_ENDPOINT: str
    DB_TOKEN: str

    model_config = SettingsConfigDict(env_file=".env")

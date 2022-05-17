from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Shelter App"
    inventory_service_url: str
    notification_service_url: str
    database_url: str
    debug: bool

    class Config:
        env_file = ".env"


@lru_cache()
def get_config() -> Settings:
    return Settings()

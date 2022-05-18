"""
    ..synopsis:: Config file for shortener_app.
"""
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    ..note::
        This class is used to configure the app.
    """

    env_name: str = "local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = "../.env"


@lru_cache
def get_settings() -> Settings:
    """
    ..note::
        This function is used to get the settings.
    """
    settings = Settings()
    print(f"Loading settings from {settings.env_name} environment.")
    return settings

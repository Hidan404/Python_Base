from pydantic import BaseSettings


class Settings(BaseSettings):
    API : str = "api/v1"
    DB_URL = ""
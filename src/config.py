from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_URL: str = "sqlite:///../posts.db:"
    DB_ECHO: bool = False


config = Config()

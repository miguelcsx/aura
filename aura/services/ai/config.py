# services/ai/ai_config.py

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    GOOGLE_API_KEY: str
    MODEL_NAME: str = "gpt2"

    class Config:
        env_file = ".env"
        extra = "ignore"


config = Config()

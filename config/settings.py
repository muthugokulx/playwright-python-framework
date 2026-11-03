import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    username: str = os.getenv("APP_USERNAME", "standard_user")
    password: str = os.getenv("APP_PASSWORD", "secret_sauce")
    default_timeout: int = int(os.getenv("DEFAULT_TIMEOUT", "10000"))


settings = Settings()

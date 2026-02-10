from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str
    db_username: str
    db_password: str
    # Add other configuration settings as needed

    class Config:
        env_file = ".env"  # use a .env file for local development
        env_file_encoding = "utf-8"

settings = Settings()
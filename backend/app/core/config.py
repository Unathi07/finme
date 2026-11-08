from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")
    app_name: str = "Finme AI API"
    app_env: str = "development"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://finme:finme_dev_only@localhost:5432/finme"
    cors_origins: str = "http://localhost:5173"


settings = Settings()


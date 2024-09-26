from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        frozen=True, case_sensitive=False,
        extra="allow",
        env_prefix="",
        env_file_encoding="utf-8",
        env_file=".env",
    )

    TOKEN: str


settings = Settings()

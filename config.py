"""Configuration placeholders for the code review agent."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    github_token: str = "YOUR_GITHUB_TOKEN"
    github_webhook_secret: str = "YOUR_GITHUB_WEBHOOK_SECRET"
    github_app_id: str = "YOUR_GITHUB_APP_ID"
    github_app_private_key_path: str = "YOUR_GITHUB_APP_PRIVATE_KEY_PATH"

    anthropic_api_key: str = "YOUR_ANTHROPIC_API_KEY"
    review_model: str = "YOUR_REVIEW_MODEL"
    embedding_model: str = "YOUR_EMBEDDING_MODEL"

    chroma_persist_directory: str = "YOUR_CHROMA_PERSIST_DIRECTORY"
    chroma_collection_name: str = "YOUR_CHROMA_COLLECTION_NAME"

    repo_owner: str = "YOUR_REPO_OWNER"
    repo_name: str = "YOUR_REPO_NAME"
    local_repo_path: str = "YOUR_LOCAL_REPO_PATH"
    default_branch: str = "YOUR_DEFAULT_BRANCH"

    log_level: str = "YOUR_LOG_LEVEL"


settings = Settings()


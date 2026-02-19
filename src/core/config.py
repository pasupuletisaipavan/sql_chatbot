from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    postgres_uri: str
    elasticsearch_host: str
    ollama_base_url: str
    embedding_model: str
    llm_model: str
    log_level: str = "info"

    class Config:
        env_file = ".env"

settings = Settings()

def get_engine():
    return create_engine(settings.postgres_uri)

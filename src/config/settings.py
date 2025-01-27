from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum

class Environment(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing"

class Settings(BaseSettings):
    # API Configuration
    API_VERSION: str = "1.0.0"
    API_TITLE: str = "CrewAI Groq API"
    
    # Required fields
    GROQ_API_KEY: str
    
    # Optional fields with defaults
    environment: Environment = Environment.DEVELOPMENT
    LOG_LEVEL: str = "INFO"
    
    # LLM Configuration
    MODEL_NAME: str = "groq/llama3-70b-8192"
    MODEL_TEMPERATURE: float = 0.3
    MODEL_MAX_TOKENS: int = 1024
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()

# Temporary debug (remove after testing)
print("\n=== LOADED SETTINGS ===")
print(f"Groq API Key: {'*' * len(settings.GROQ_API_KEY)}")
print(f"Environment: {settings.environment}\n")
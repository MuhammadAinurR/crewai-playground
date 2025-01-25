from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # REQUIRED fields (must match .env variables)
    GROQ_API_KEY: str  # <<< NOTE: UPPERCASE
    
    # Optional fields with defaults
    environment: str = "development"
    
    # Configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()  # Instantiate

# Temporary debug (remove after testing)
print("\n=== LOADED SETTINGS ===")
print(f"Groq API Key: {'*' * len(settings.GROQ_API_KEY)}")
print(f"Environment: {settings.environment}\n")
from functools import lru_cache
from .utils.groq_client import get_groq_llm
from .config.settings import Settings
from crewai import LLM

@lru_cache()
def get_settings() -> Settings:
    return Settings()

@lru_cache()
def get_llm() -> LLM:
    return get_groq_llm() 
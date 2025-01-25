from crewai import LLM
from src.config.settings import settings

def get_groq_llm():
    return LLM(
        model="groq/llama3-70b-8192",
        api_key=settings.GROQ_API_KEY,  # UPPERCASE
        temperature=0.3,
        max_tokens=1024
    )
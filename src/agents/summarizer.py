from crewai import Agent
from ..config import settings
from ..utils.groq_client import get_groq_llm

def create_summarizer():
    return Agent(
        role='Senior Documentation Engineer',
        goal='Produce crystal-clear technical summaries',
        backstory='Expert technical writer with decade of experience in API documentation',
        llm=get_groq_llm(),
        verbose=True,
        memory=True
    )
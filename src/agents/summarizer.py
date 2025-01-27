from crewai import Agent
from ..config import settings
from ..utils.groq_client import get_groq_llm

def create_summarizer() -> Agent:
    """
    Creates a documentation summarizer agent specialized in technical writing.
    
    Returns:
        Agent: A CrewAI agent configured for documentation summarization.
    """
    return Agent(
        role='Senior Documentation Engineer',
        goal='Produce crystal-clear technical summaries',
        backstory="""Expert technical writer with decade of experience in API documentation, 
                    specializing in clear and concise technical communication""",
        llm=get_groq_llm(),
        verbose=True,  # Using direct boolean instead of settings
        memory=True
    )
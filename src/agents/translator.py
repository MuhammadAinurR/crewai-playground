from crewai import Agent
from ..utils.groq_client import get_groq_llm

def create_translator() -> Agent:
    """
    Creates a translator agent specialized in language translation.
    
    Returns:
        Agent: A CrewAI agent configured for translation tasks.
    """
    return Agent(
        role='Professional Translator',
        goal='Provide accurate and natural-sounding translations',
        backstory="""Expert linguist and translator with extensive experience in 
                    multiple languages and cultural nuances. Specialized in 
                    maintaining context and meaning in translations.""",
        llm=get_groq_llm(),
        verbose=True,
        memory=True
    ) 
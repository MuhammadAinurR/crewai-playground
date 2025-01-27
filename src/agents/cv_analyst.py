from crewai import Agent
from ..utils.groq_client import get_groq_llm

def create_cv_analyst() -> Agent:
    """Creates a CV analysis specialist agent."""
    return Agent(
        role='Senior HR Consultant & Career Coach',
        goal='Provide comprehensive CV analysis and improvement recommendations',
        backstory="""Experienced HR professional and career coach with 15+ years 
                    of experience in resume optimization, career development, and 
                    recruitment across multiple industries. Expert in identifying 
                    CV strengths and areas for improvement.""",
        llm=get_groq_llm(),
        verbose=True,
        memory=True
    ) 
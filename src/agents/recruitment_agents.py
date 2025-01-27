from crewai import Agent
from ..utils.groq_client import get_groq_llm

def create_criteria_analyst() -> Agent:
    """Creates an agent specialized in analyzing job descriptions and creating assessment criteria."""
    return Agent(
        role='Senior Technical Recruiter',
        goal='Create comprehensive assessment criteria from job descriptions',
        backstory="""Expert in technical recruitment with deep understanding of 
                    software engineering roles and requirements. Specialized in 
                    creating detailed assessment frameworks.""",
        llm=get_groq_llm(),
        verbose=True
    )

def create_interviewer() -> Agent:
    """Creates an agent specialized in technical interviews."""
    return Agent(
        role='Technical Interview Specialist',
        goal='Conduct in-depth technical interviews and assess candidates',
        backstory="""Experienced technical leader with deep expertise in 
                    software engineering and system design. Skilled at 
                    evaluating technical depth and problem-solving abilities.""",
        llm=get_groq_llm(),
        verbose=True
    )

def create_evaluator() -> Agent:
    """Creates an agent specialized in evaluating interview responses."""
    return Agent(
        role='Technical Assessment Specialist',
        goal='Evaluate technical responses and provide detailed feedback',
        backstory="""Expert in technical assessment with experience in 
                    evaluating software engineering capabilities and providing 
                    constructive feedback.""",
        llm=get_groq_llm(),
        verbose=True
    ) 
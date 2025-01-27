from crewai import Task, Agent
from typing import Optional

DEFAULT_CRITERIA_FORMAT = '''{
    "technical_skills": [
        {"skill_name": "required_level"}
    ],
    "experience_requirements": [
        "list of specific experience requirements"
    ],
    "key_competencies": [
        "list of required competencies"
    ],
    "evaluation_metrics": {
        "category": ["specific metrics"]
    }
}'''

DEFAULT_QUESTIONS_FORMAT = '''{
    "technical_questions": [
        {
            "question": "detailed technical question",
            "context": "why this is being asked",
            "expected_points": ["key points to look for in answer"]
        }
    ],
    "experience_questions": [
        {
            "question": "experience-based question",
            "context": "relevant experience to verify",
            "expected_points": ["key points to look for in answer"]
        }
    ],
    "problem_solving_questions": [
        {
            "question": "scenario-based question",
            "context": "problem-solving aspect being tested",
            "expected_points": ["key points to look for in answer"]
        }
    ]
}'''

DEFAULT_EVALUATION_FORMAT = '''{
    "technical_accuracy": {
        "score": "0-100",
        "comments": "detailed assessment"
    },
    "understanding_depth": {
        "score": "0-100",
        "comments": "evaluation of understanding"
    },
    "practical_experience": {
        "score": "0-100",
        "comments": "assessment of hands-on experience"
    },
    "overall_feedback": "comprehensive feedback",
    "recommendations": ["specific improvement points"]
}'''

def create_criteria_analysis_task(
    job_description: str,
    agent: Agent
) -> Task:
    """Creates assessment criteria from job description."""
    return Task(
        description=f"""Analyze this job description and create detailed assessment criteria:
        {job_description}
        
        Create criteria that covers:
        1. Technical skills assessment framework
        2. Experience verification approach
        3. Problem-solving evaluation metrics
        4. Key competencies to evaluate
        
        Focus on creating criteria that can verify real experience versus theoretical knowledge.""",
        expected_output=DEFAULT_CRITERIA_FORMAT,
        agent=agent
    )

def create_interview_questions_task(
    cv_text: str,
    assessment_criteria: dict,
    agent: Agent
) -> Task:
    """Generates interview questions based on CV and criteria."""
    return Task(
        description=f"""Based on this CV and assessment criteria, create in-depth interview questions:
        
        CV: {cv_text}
        
        Criteria: {assessment_criteria}
        
        Generate questions that:
        1. Verify claimed experience with specific technical scenarios
        2. Probe problem-solving abilities
        3. Assess depth of knowledge in key technologies
        4. Evaluate past project challenges and solutions""",
        expected_output=DEFAULT_QUESTIONS_FORMAT,
        agent=agent
    )

def create_response_evaluation_task(
    question: str,
    response: str,
    criteria: dict,
    agent: Agent
) -> Task:
    """Evaluates candidate responses."""
    return Task(
        description=f"""Evaluate this response against our assessment criteria:
        
        Question: {question}
        Response: {response}
        Criteria: {criteria}
        
        Provide:
        1. Technical accuracy assessment
        2. Depth of understanding evaluation
        3. Problem-solving capability analysis
        4. Specific feedback and observations""",
        expected_output=DEFAULT_EVALUATION_FORMAT,
        agent=agent
    ) 
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
    "conversation_flows": [
        {
            "initial_topic": "Redis Implementation",
            "base_question": "Can you explain how you've implemented Redis in your projects?",
            "follow_up_questions": [
                {
                    "trigger": "caching",
                    "question": "What happens when Redis hits memory limits in your implementation?",
                    "deeper_questions": [
                        "How do you handle Redis cache eviction policies?",
                        "What strategies have you implemented for scaling Redis?",
                        "How do you ensure Redis high availability in production?"
                    ]
                },
                {
                    "trigger": "queue",
                    "question": "How do you prevent Redis from becoming a SPOF when used as a queue?",
                    "deeper_questions": [
                        "What backup mechanisms do you implement?",
                        "How do you handle failed jobs?",
                        "What monitoring systems do you use?"
                    ]
                }
            ],
            "exit_conditions": [
                "Cannot explain scaling strategies",
                "Limited understanding of HA concepts",
                "Unclear about monitoring approaches"
            ]
        }
    ],
    "assessment_points": {
        "technical_depth": "How deep into technical details they can go",
        "problem_solving": "How they approach scaling and reliability issues",
        "experience": "Real-world examples and challenges they've faced"
    }
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
    """Generates dynamic interview conversation flows."""
    return Task(
        description=f"""Create a dynamic technical interview plan based on this CV and criteria:
        
        CV: {cv_text}
        Criteria: {assessment_criteria}
        
        For each major skill/technology mentioned:
        1. Start with a base question about their experience
        2. Create follow-up questions that go progressively deeper
        3. Include technical challenges and edge cases
        4. Define points where to guide the candidate if they struggle
        5. Identify when to move to the next topic
        
        Make questions:
        - Progressive (each answer leads to a deeper technical discussion)
        - Experience-based (focus on real scenarios they've handled)
        - Problem-solving oriented (how they handle limitations/issues)
        
        The interview should feel like a natural technical discussion that 
        gets progressively more challenging until the candidate's knowledge limit is reached.""",
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
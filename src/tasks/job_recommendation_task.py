from crewai import Task, Agent

DEFAULT_OUTPUT_FORMAT = '''{
    "recommendations": [
        {
            "title": "Job Title",
            "match_score": 0.95,
            "key_matches": ["matching", "skills", "here"],
            "description": "Job description",
            "required_skills": ["required", "skills"],
            "recommended_skills": ["skills", "to", "learn"]
        }
    ],
    "summary": "Overall career path recommendation summary"
}'''

def create_job_recommendation_task(
    cv_text: str,
    agent: Agent,
    expected_output: str = DEFAULT_OUTPUT_FORMAT
) -> Task:
    """Creates a job recommendation task based on CV analysis."""
    
    task_description = f"""Analyze this CV/resume and recommend suitable jobs:

{cv_text}

Please analyze the CV and:
1. Identify the most suitable job roles based on skills and experience
2. Calculate match scores based on skill alignment
3. Identify key matching skills for each role
4. Suggest additional skills that would enhance candidacy
5. Provide a career path recommendation summary

Focus on technical roles that match the candidate's skill set and experience level."""

    return Task(
        description=task_description,
        expected_output=expected_output,
        agent=agent,
        async_execution=False
    ) 
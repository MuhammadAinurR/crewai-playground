from typing import Optional
from crewai import Task, Agent

DEFAULT_OUTPUT_FORMAT = '''{
    "summary": "Brief CV overview",
    "strengths": ["list", "of", "strengths"],
    "improvements": ["suggested", "improvements"],
    "skills_analysis": {
        "technical": ["skills", "assessment"],
        "soft": ["skills", "assessment"]
    },
    "recommendations": ["specific", "actionable", "recommendations"]
}'''

def create_cv_analysis_task(
    cv_text: str,
    agent: Agent,
    expected_output: str = DEFAULT_OUTPUT_FORMAT
) -> Task:
    """Creates a CV analysis task."""
    
    task_description = f"""Analyze this CV/resume and provide detailed feedback:

{cv_text}

Please analyze the CV for:
1. Overall impression and summary
2. Key strengths
3. Areas for improvement
4. Skills analysis (both technical and soft skills)
5. Specific recommendations for enhancement

Structure your response as a JSON object with:
1. A 'summary' field with brief CV overview
2. A 'strengths' array listing strong points
3. An 'improvements' array listing areas needing work
4. A 'skills_analysis' object with 'technical' and 'soft' skill arrays
5. A 'recommendations' array with specific actionable items"""

    return Task(
        description=task_description,
        expected_output=expected_output,
        agent=agent,
        async_execution=False
    ) 
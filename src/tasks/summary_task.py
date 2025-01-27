from typing import Dict, List, Optional
from crewai import Task, Agent

DEFAULT_OUTPUT_FORMAT = '''{
    "summary": "concise markdown summary",
    "key_points": ["array", "of", "bullet points"]
}'''

def create_summary_task(
    documentation: str,
    agent: Agent,
    expected_output: str = DEFAULT_OUTPUT_FORMAT,
    target_language: Optional[str] = None
) -> Task:
    """
    Creates a documentation summarization task.

    Args:
        documentation (str): The documentation text to be summarized
        agent (Agent): The agent responsible for summarization
        expected_output (str, optional): Expected JSON structure format. 
            Defaults to DEFAULT_OUTPUT_FORMAT.
        target_language (str, optional): Target language for translation.
            If provided, the summary will be translated to this language.

    Returns:
        Task: A CrewAI task configured for documentation summarization
    """
    language_instruction = (
        f"\nPlease provide the summary and key points in {target_language} language."
        if target_language
        else ""
    )

    task_description = f"""Analyze and summarize this documentation:

{documentation}

Please structure your response as a JSON object with:
1. A 'summary' field containing a concise markdown summary
2. A 'key_points' array containing the main takeaways as bullet points{language_instruction}"""

    return Task(
        description=task_description,
        expected_output=expected_output,
        agent=agent,
        async_execution=False
    )
from typing import Optional
from crewai import Task, Agent

DEFAULT_OUTPUT_FORMAT = '''{
    "translated_text": "the translated content",
    "source_language": "detected source language",
    "target_language": "target language"
}'''

def create_translation_task(
    text: str,
    target_language: str,
    agent: Agent,
    expected_output: str = DEFAULT_OUTPUT_FORMAT
) -> Task:
    """
    Creates a translation task.

    Args:
        text (str): The text to be translated
        target_language (str): Target language for translation
        agent (Agent): The agent responsible for translation
        expected_output (str, optional): Expected JSON structure format

    Returns:
        Task: A CrewAI task configured for translation
    """
    task_description = f"""Translate the following text to {target_language}:

{text}

Please structure your response as a JSON object with:
1. A 'translated_text' field containing the translation
2. A 'source_language' field indicating the detected source language
3. A 'target_language' field confirming the target language"""

    return Task(
        description=task_description,
        expected_output=expected_output,
        agent=agent,
        async_execution=False
    ) 
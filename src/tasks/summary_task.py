from crewai import Task, Agent

def create_summary_task(
    documentation: str,
    agent: Agent,
    expected_output: str = '''{
        "summary": "concise markdown summary",
        "key_points": ["array", "of", "bullet points"]
    }'''
) -> Task:
    return Task(
        description=f"""Analyze and summarize this documentation:

{documentation}

Please structure your response as a JSON object with:
1. A 'summary' field containing a concise markdown summary
2. A 'key_points' array containing the main takeaways as bullet points""",
        expected_output=expected_output,
        agent=agent,
        async_execution=False
    )
from crewai import Task, Agent
# In src/tasks/translation_task.py
def create_translation_task(
    text: str,
    agent: Agent,  # Pass agent here too
    target_language: str
) -> Task:
    return Task(
        description=f"Translate to {target_language}: {text}",
        agent=agent,
        dependencies=[...]
    )
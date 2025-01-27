from typing import List, Optional, Any
from pydantic import BaseModel, Field
import json

class TaskOutput(BaseModel):
    """Model for individual task output details."""
    description: str
    name: Optional[str]
    expected_output: str
    summary: str
    raw: str
    pydantic: Optional[Any]
    json_dict: Optional[Any]
    agent: str
    output_format: str

class TokenUsage(BaseModel):
    """Pydantic model for token usage statistics."""
    total_tokens: int
    prompt_tokens: int
    cached_prompt_tokens: int
    completion_tokens: int
    successful_requests: int

class CrewResult(BaseModel):
    """Model for the raw crew execution result."""
    raw: str
    pydantic: Optional[Any]
    json_dict: Optional[Any]
    tasks_output: List[TaskOutput]
    token_usage: TokenUsage

class SummaryResponse(BaseModel):
    summary: str
    key_points: List[str]

class SummaryResult(BaseModel):
    result: Any

    def model_dump(self):
        # Parse the raw JSON string from CrewAI's output
        try:
            parsed_result = json.loads(self.result.raw)
            return SummaryResponse(
                summary=parsed_result["summary"],
                key_points=parsed_result["key_points"]
            ).model_dump()
        except Exception:
            return super().model_dump()

    class Config:
        arbitrary_types_allowed = True
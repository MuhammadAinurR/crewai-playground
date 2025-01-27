from typing import List, Dict, Any
from pydantic import BaseModel
import json

class CVAnalysisResponse(BaseModel):
    summary: str
    strengths: List[str]
    improvements: List[str]
    skills_analysis: Dict[str, List[str]]
    recommendations: List[str]

class CVAnalysisResult(BaseModel):
    result: Any

    class Config:
        arbitrary_types_allowed = True

    def model_dump(self, **kwargs):
        try:
            raw_json = self.result.raw if hasattr(self.result, 'raw') else self.result
            parsed_result = json.loads(raw_json)
            return CVAnalysisResponse(**parsed_result).model_dump()
        except Exception:
            return super().model_dump(**kwargs)
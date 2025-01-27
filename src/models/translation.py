from pydantic import BaseModel
from typing import Any
import json

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class TranslationResponse(BaseModel):
    translated_text: str
    source_language: str
    target_language: str

class TranslationResult(BaseModel):
    result: Any

    class Config:
        arbitrary_types_allowed = True

    def model_dump(self, **kwargs):
        try:
            raw_json = self.result.raw if hasattr(self.result, 'raw') else self.result
            parsed_result = json.loads(raw_json)
            return TranslationResponse(
                translated_text=parsed_result["translated_text"],
                source_language=parsed_result["source_language"],
                target_language=parsed_result["target_language"]
            ).model_dump()
        except Exception:
            return super().model_dump(**kwargs) 
from typing import List
from pydantic import BaseModel

class JobRecommendation(BaseModel):
    title: str
    match_score: float
    key_matches: List[str]
    description: str
    required_skills: List[str]
    recommended_skills: List[str]

class JobRecommendationsResponse(BaseModel):
    recommendations: List[JobRecommendation]
    summary: str 
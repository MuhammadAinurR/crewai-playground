from typing import List, Dict, Optional
from pydantic import BaseModel

class JobDescription(BaseModel):
    title: str
    description: str
    requirements: List[str]
    responsibilities: List[str]

class AssessmentCriteria(BaseModel):
    technical_skills: List[Dict[str, str]]  # skill: required_level
    experience_requirements: List[str]
    key_competencies: List[str]
    evaluation_metrics: Dict[str, List[str]]

class InterviewQuestion(BaseModel):
    question: str
    context: str
    expected_answer_points: List[str]
    difficulty_level: str
    category: str

class CandidateResponse(BaseModel):
    question_id: str
    response: str

class AssessmentResult(BaseModel):
    technical_score: float
    experience_depth: float
    problem_solving: float
    detailed_feedback: Dict[str, str]
    recommendations: List[str]
    overall_assessment: str 
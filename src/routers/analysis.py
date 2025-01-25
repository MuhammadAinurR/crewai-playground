from fastapi import APIRouter, HTTPException
from ..agents.summarizer import create_summarizer
from ..tasks.summary_task import create_summary_task
from src.config.settings import settings
from crewai import Crew

router = APIRouter(prefix="/api/v1", tags=["analysis"])

@router.get("/health")
async def health_check():
    return {"status": "ok", "environment": settings.environment}

@router.post("/analyze")
async def analyze_documentation(payload: dict):
    try:
        # Create agent FIRST
        summarizer = create_summarizer()
        
        # Create task WITH AGENT REFERENCE
        summary_task = create_summary_task(
            documentation=payload['documentation'],
            agent=summarizer  # <-- Critical fix
        )
        
        crew = Crew(
            agents=[summarizer],
            tasks=[summary_task],
            verbose=True
        )
        
        result = crew.kickoff()
        return {"result": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")
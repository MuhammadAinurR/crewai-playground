from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import json

from ..agents.summarizer import create_summarizer
from ..tasks.summary_task import create_summary_task
from ..models.summary import SummaryResult, SummaryResponse
from ..config.settings import settings, Settings, Environment
from crewai import Crew
from ..dependencies import get_settings, get_llm
from ..utils.logger import setup_logger

logger = setup_logger(__name__)
router = APIRouter(prefix="/api/v1", tags=["analysis"])

class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    environment: str

class AnalysisRequest(BaseModel):
    """Analysis request model."""
    documentation: str
    target_language: Optional[str] = None

@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Check the health status of the API.
    
    Returns:
        HealthResponse: Current status and environment information
    """
    return HealthResponse(
        status="ok",
        environment=settings.environment
    )

@router.post("/analyze", response_model=SummaryResponse)
async def analyze_documentation(
    payload: AnalysisRequest,
    settings: Settings = Depends(get_settings)
) -> SummaryResponse:
    """
    Analyze and summarize the provided documentation.
    
    Args:
        payload (AnalysisRequest): Request containing documentation and optional target language
    
    Returns:
        SummaryResponse: Contains the summary and key points
        
    Raises:
        HTTPException: If there's an error processing the documentation
    """
    logger.info("Starting documentation analysis")
    try:
        summarizer = create_summarizer()
        summary_task = create_summary_task(
            documentation=payload.documentation,
            agent=summarizer,
            target_language=payload.target_language
        )
        
        crew = Crew(
            agents=[summarizer],
            tasks=[summary_task],
            verbose=settings.environment == Environment.DEVELOPMENT
        )
        
        result = crew.kickoff()
        logger.info("Analysis completed successfully")
        
        # Parse the result directly
        parsed_result = json.loads(result.raw)
        return SummaryResponse(
            summary=parsed_result["summary"],
            key_points=parsed_result["key_points"]
        )
    
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Processing error: {str(e)}"
        )
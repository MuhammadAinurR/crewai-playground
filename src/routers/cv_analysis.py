from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from ..models.cv_analysis import CVAnalysisResponse
from ..agents.cv_analyst import create_cv_analyst
from ..tasks.cv_analysis_task import create_cv_analysis_task
from ..config.settings import Settings, Environment
from ..dependencies import get_settings
from ..utils.logger import setup_logger
from crewai import Crew
import PyPDF2
import io
import json

logger = setup_logger(__name__)
router = APIRouter(prefix="/api/v1", tags=["cv-analysis"])

@router.post("/analyze-cv", response_model=CVAnalysisResponse)
async def analyze_cv(
    cv_file: UploadFile = File(...),
    settings: Settings = Depends(get_settings)
) -> CVAnalysisResponse:
    """
    Analyze a CV/resume PDF and provide improvement recommendations.
    """
    logger.info(f"Starting CV analysis for file: {cv_file.filename}")
    
    # Validate file type
    if not cv_file.filename.endswith('.pdf'):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )
    
    try:
        # Read PDF content
        pdf_content = await cv_file.read()
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))
        
        # Extract text from all pages
        cv_text = ""
        for page in pdf_reader.pages:
            cv_text += page.extract_text()
        
        # Create and execute analysis task
        analyst = create_cv_analyst()
        analysis_task = create_cv_analysis_task(
            cv_text=cv_text,
            agent=analyst
        )
        
        crew = Crew(
            agents=[analyst],
            tasks=[analysis_task],
            verbose=settings.environment == Environment.DEVELOPMENT
        )
        
        result = crew.kickoff()
        logger.info("CV analysis completed successfully")
        
        parsed_result = json.loads(result.raw)
        return CVAnalysisResponse(**parsed_result)
    
    except Exception as e:
        logger.error(f"Error during CV analysis: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"CV analysis error: {str(e)}"
        ) 
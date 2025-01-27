from fastapi import APIRouter, HTTPException, Depends
from ..models.translation import TranslationRequest, TranslationResponse
from ..agents.translator import create_translator
from ..tasks.translation_task import create_translation_task
from ..config.settings import Settings, Environment
from crewai import Crew
from ..dependencies import get_settings
from ..utils.logger import setup_logger
import json

logger = setup_logger(__name__)
router = APIRouter(prefix="/api/v1", tags=["translation"])

@router.post("/translate", response_model=TranslationResponse)
async def translate_text(
    payload: TranslationRequest,
    settings: Settings = Depends(get_settings)
) -> TranslationResponse:
    """
    Translate text to the specified target language.
    """
    logger.info(f"Starting translation to {payload.target_language}")
    try:
        translator = create_translator()
        translation_task = create_translation_task(
            text=payload.text,
            target_language=payload.target_language,
            agent=translator
        )
        
        crew = Crew(
            agents=[translator],
            tasks=[translation_task],
            verbose=settings.environment == Environment.DEVELOPMENT
        )
        
        result = crew.kickoff()
        logger.info("Translation completed successfully")
        
        parsed_result = json.loads(result.raw)
        return TranslationResponse(
            translated_text=parsed_result["translated_text"],
            source_language=parsed_result["source_language"],
            target_language=parsed_result["target_language"]
        )
    
    except Exception as e:
        logger.error(f"Error during translation: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Translation error: {str(e)}"
        ) 
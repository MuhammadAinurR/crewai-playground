from fastapi import APIRouter, HTTPException, Depends, File, UploadFile, Form
from ..models.recruitment import *
from ..agents.recruitment_agents import *
from ..tasks.recruitment_tasks import *
from crewai import Crew
import json
import PyPDF2
import io
from ..utils.interview_logic import InterviewLogicHandler

router = APIRouter(prefix="/api/v1/recruitment", tags=["recruitment"])

@router.post("/analyze-job", response_model=AssessmentCriteria)
async def create_assessment_criteria(job_desc: JobDescription):
    """Create assessment criteria from job description"""
    try:
        analyst = create_criteria_analyst()
        task = create_criteria_analysis_task(
            job_description=job_desc.model_dump_json(),
            agent=analyst
        )
        crew = Crew(agents=[analyst], tasks=[task])
        result = crew.kickoff()
        return json.loads(result.raw)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-questions")
async def generate_interview_questions(
    cv_file: UploadFile = File(...),
    criteria: str = Form(...)
):
    """Generate interview questions based on CV and criteria"""
    try:
        # Read PDF content properly
        pdf_content = await cv_file.read()
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))
        
        # Extract text from all pages
        cv_text = ""
        for page in pdf_reader.pages:
            cv_text += page.extract_text()

        criteria_dict = json.loads(criteria)
        
        interviewer = create_interviewer()
        task = create_interview_questions_task(
            cv_text=cv_text,
            assessment_criteria=criteria_dict,
            agent=interviewer
        )
        crew = Crew(agents=[interviewer], tasks=[task])
        return json.loads(crew.kickoff().raw)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/evaluate-response")
async def evaluate_response(
    question_id: str = Form(...),
    response: str = Form(...),
    criteria: str = Form(...),
    conversation_flows: str = Form(...),
    current_question_level: str = Form(default="base")
):
    """Evaluate candidate's response and determine next question"""
    try:
        # Existing evaluation logic
        criteria_dict = json.loads(criteria)
        conversation_flows_dict = json.loads(conversation_flows)
        evaluator = create_evaluator()
        task = create_response_evaluation_task(
            question=question_id,
            response=response,
            criteria=criteria_dict,
            agent=evaluator
        )
        crew = Crew(agents=[evaluator], tasks=[task])
        evaluation = json.loads(crew.kickoff().raw)

        # Get next question using interview logic
        interview_handler = InterviewLogicHandler(conversation_flows_dict["conversation_flows"])
        next_question_type, next_question, deeper_questions = (
            interview_handler.select_next_question(
                topic=question_id,
                response=response,
                evaluation=evaluation,
                current_question_level=current_question_level
            )
        )

        # Add next question information to response
        evaluation["next_question"] = {
            "type": next_question_type,
            "question": next_question,
            "deeper_questions": deeper_questions
        }

        return evaluation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
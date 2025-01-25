from fastapi import FastAPI
from .routers import analysis
from .config import settings

app = FastAPI(
    title="CrewAI Groq API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
)

# Include routers
app.include_router(analysis.router)

@app.get("/")
async def root():
    return {"message": "CrewAI Groq API Service"}
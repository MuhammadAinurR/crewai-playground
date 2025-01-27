from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import analysis, translation, cv_analysis
from .config.settings import settings
from .utils.logger import setup_logger

logger = setup_logger(__name__)

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    docs_url="/docs",
    redoc_url=None
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(analysis.router)
app.include_router(translation.router)
app.include_router(cv_analysis.router)

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.API_TITLE} in {settings.environment} mode")

@app.get("/")
async def root():
    return {"message": f"{settings.API_TITLE} Service"}
from fastapi import FastAPI
from app.core.config import get_settings
from app.api.endpoints import router

app = FastAPI(
    title=get_settings().PROJECT_NAME,
    version=get_settings().VERSION
)

# Include routers
app.include_router(router)

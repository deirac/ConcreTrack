from fastapi import APIRouter
from app.api.endpoints.users import router as users_router
from app.api.endpoints.auth import router as auth_router
from app.core.config import get_settings

router = APIRouter()

# include routers under API v1 prefix
api_v1 = get_settings().API_V1_STR
router.include_router(users_router, prefix=api_v1)
router.include_router(auth_router, prefix=api_v1)
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_users():
    return {"message": "List users endpoint"}
from fastapi import APIRouter, Depends
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def register_user(user: UserCreate):
    return await create_user(user)

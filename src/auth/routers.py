from fastapi import APIRouter
from schemas import UserCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from services import UserService
auth_router = APIRouter
user_service=UserService()
@auth_router.post('/signup')
async def signup(user_data:UserCreateModel,session:AsyncSession):
    pass
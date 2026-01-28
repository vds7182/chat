from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import User
from schemas import UserCreateModel,UserLogin
class UserService:
    async def get_user(self, user_email:str,session:AsyncSession):
        statement = select(User).where(User.email == user_email)
        result = await session.exec(statement)
        return result.first()
    async def create_user(self,user_model:UserCreateModel ,session:AsyncSession):
        user= user_model.model_dump()
        new_user=User(**user)
        new_user.password_hash=hash(user['password'])
        session.add(new_user)
        await session.commit()
        return new_user


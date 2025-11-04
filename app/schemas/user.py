from typing import Optional
from pydantic import BaseModel, EmailStr
from app.core.enums import Role


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str
    # allow role on create, default to client
    role: Optional[Role] = Role.client


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    is_active: bool
    role: Role

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
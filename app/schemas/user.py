from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, StringConstraints, Field
from app.core.enums import Role


class UserBase(BaseModel):
    email: EmailStr
    username: Annotated[str, StringConstraints(min_length=3, max_length=50)]


class UserCreate(UserBase):
    password: Annotated[str, StringConstraints(min_length=8, max_length=72)]
    # allow role on create, default to client
    role: Optional[Role] = Role.client

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "password": "strongpass123",
                "role": "client"
            }
        }


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


# FormulaTeorica schemas moved to app/schemas/formulas.py
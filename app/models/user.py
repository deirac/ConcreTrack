from sqlalchemy import Column, Integer, String, Boolean, Enum as SAEnum, Date, Time, Float
from sqlalchemy.ext.declarative import declarative_base
from app.core.enums import Role

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    # role: one of Role values (super, admin, operator, client)
    role = Column(SAEnum(Role, name="role_enum"), default=Role.client, nullable=False)
    
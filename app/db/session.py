from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(
    get_settings().DATABASE_URL,
    connect_args={"check_same_thread": False}  # Solo para SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
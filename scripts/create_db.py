"""
Script to initialize the database. Run this file directly:
python create_db.py
"""
import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from app.db.session import engine
from app.models.user import Base

def init_db():
    # Create database directory if it doesn't exist
    db_dir = Path(project_root) / "data"
    db_dir.mkdir(exist_ok=True)
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()
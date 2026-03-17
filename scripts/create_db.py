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

from app.db.session import engine, Base
from app.models.user import User
from app.models.pedido import Pedido
from app.models.formulas import FormulaTeorica, FormulaReal

def init_db():
    try: 
        # Create database directory if it doesn't exist
        db_dir = Path(project_root) / "data"
        db_dir.mkdir(exist_ok=True)
        print(f"📁 Directorio de BD: {db_dir.absolute()}")

        # Create all tables
        print("🔧 Creating database tables...")
        Base.metadata.create_all(bind=engine)

        # User.metadata.create_all(bind=engine)
        # Pedido.metadata.create_all(bind=engine)
        # FormulaTeorica.metadata.create_all(bind=engine)
        # FormulaReal.metadata.create_all(bind=engine)

        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print("✅ Tablas en la base de datos:")
        for table in tables:
            print(f" - {table}")
    except Exception as e:
        print("❌ Error initializing database:", e)
        raise

if __name__ == "__main__":
    init_db()
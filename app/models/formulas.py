from sqlalchemy import Column, Integer, Date, Time, Float, Index
from app.db.session import Base


class FormulaMixin:
    """Common columns for both theoretical and real formula tables."""
    
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=True, index=True)
    hora = Column(Time, nullable=True)

    # Material measurements
    arena = Column(Float, nullable=True)
    agua = Column(Float, nullable=True)
    adt1 = Column(Float, nullable=True)
    adt2 = Column(Float, nullable=True)
    cmto = Column(Float, nullable=True)
    adic = Column(Float, nullable=True)
    grava = Column(Float, nullable=True)
    
    # Concrete properties
    resistencia = Column(Float, nullable=True, comment="Resistencia del concreto en kg/cm²")


class FormulaTeorica(FormulaMixin, Base):
    """SQLAlchemy model for theoretical formula values."""
    __tablename__ = "formula_teorica"
    
    # Create an index on fecha and hora for efficient datetime queries
    __table_args__ = (
        Index('ix_formula_teorica_fecha_hora', 'fecha', 'hora'),
    )


class FormulaReal(FormulaMixin, Base):
    """SQLAlchemy model for real/actual formula measurements."""
    __tablename__ = "formula_real"
    
    # Create an index on fecha and hora for efficient datetime queries
    __table_args__ = (
        Index('ix_formula_real_fecha_hora', 'fecha', 'hora'),
    )

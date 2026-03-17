from typing import Optional
from datetime import date, time
from pydantic import BaseModel, Field


class FormulaBase(BaseModel):
    """Base schema for both theoretical and real formula measurements."""
    
    fecha: Optional[date] = Field(
        default=None,
        description="Date when the formula was created/measured"
    )
    hora: Optional[time] = Field(
        default=None,
        description="Time when the formula was created/measured"
    )

    # Material measurements with validation
    arena: Optional[float] = Field(
        default=None, ge=0,
        description="Arena measurement in kg"
    )
    agua: Optional[float] = Field(
        default=None, ge=0,
        description="Agua measurement in L"
    )
    adt1: Optional[float] = Field(
        default=None, ge=0,
        description="ADT1 additive measurement in kg"
    )
    adt2: Optional[float] = Field(
        default=None, ge=0,
        description="ADT2 additive measurement in kg"
    )
    cmto: Optional[float] = Field(
        default=None, ge=0,
        description="Cemento measurement in kg"
    )
    adic: Optional[float] = Field(
        default=None, ge=0,
        description="Aditivo measurement in kg"
    )
    grava: Optional[float] = Field(
        default=None, ge=0,
        description="Grava measurement in kg"
    )


class FormulaTeoricaCreate(FormulaBase):
    """Schema for creating a new theoretical formula."""
    class Config:
        json_schema_extra = {
            "example": {
                "fecha": "2025-11-04",
                "hora": "14:30:00",
                "arena": 100.5,
                "agua": 50.0,
                "adt1": 2.5,
                "adt2": 1.5,
                "cmto": 75.0,
                "adic": 1.0,
                "grava": 150.0
            }
        }

class FormulaTeorica(FormulaBase):
    """Schema for reading a theoretical formula with ID."""
    id: int

    class Config:
        from_attributes = True

class FormulaRealCreate(FormulaBase):
    """Schema for creating a new real/actual formula measurement."""
    class Config:
        json_schema_extra = {
            "example": {
                "fecha": "2025-11-04",
                "hora": "14:35:00",
                "arena": 98.5,
                "agua": 51.0,
                "adt1": 2.4,
                "adt2": 1.6,
                "cmto": 74.5,
                "adic": 1.1,
                "grava": 149.5
            }
        }

class FormulaReal(FormulaBase):
    """Schema for reading a real formula measurement with ID."""
    id: int

    class Config:
        from_attributes = True

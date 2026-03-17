from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.formulas import FormulaTeorica as FormulaModel
from app.schemas.formulas import FormulaTeorica, FormulaTeoricaCreate

router = APIRouter(prefix="/formulas", tags=["formulas"])


@router.post("/", response_model=FormulaTeorica, status_code=status.HTTP_201_CREATED)
def create_formula(
    *, db: Session = Depends(get_db), formula_in: FormulaTeoricaCreate
) -> FormulaTeorica:
    formula = FormulaModel(**formula_in.model_dump())
    db.add(formula)
    db.commit()
    db.refresh(formula)
    return formula


@router.get("/", response_model=List[FormulaTeorica])
def list_formulas(db: Session = Depends(get_db)) -> List[FormulaTeorica]:
    return db.query(FormulaModel).all()


@router.get("/{formula_id}", response_model=FormulaTeorica)
def get_formula(formula_id: int, db: Session = Depends(get_db)) -> FormulaTeorica:
    formula = db.query(FormulaModel).filter(FormulaModel.id == formula_id).first()
    if not formula:
        raise HTTPException(status_code=404, detail="Formula not found")
    return formula

"""Income API endpoints


Unauthenticated and local-only until authenticated"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy import select
from sqlalchemy.orm import Session

# Importing all the necessary modules
from app.db.session import get_db
from app.models.income import Income
from app.schemas.income import IncomeCreate, IncomeRead, IncomeUpdate

router = APIRouter(prefix="/income", tags=["income"])

DbSession = Annotated[Session, Depends(get_db)]
IncomeId = Annotated[int, Path(ge=1, le=2_147_483_647)]


def _get_or_404(db: Session, income_id: int) -> Income:
    income = db.get(Income, income_id)
    if income is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Income not found",
        )
    return income


@router.get("", response_model=list[IncomeRead])
def list_income(
    db: DbSession,
    limit: Annotated[int, Query(ge=1, le=500)] = 100,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> list[Income]:
    stmt = (
        select(Income)
        .order_by(Income.received_on.desc(), Income.id.desc())
        .limit(limit)
        .offset(offset)
    )
    return list(db.scalars(stmt))


@router.post("", response_model=IncomeRead, status_code=status.HTTP_201_CREATED)
def create_income(payload: IncomeCreate, db: DbSession) -> Income:
    income = Income(**payload.model_dump())
    db.add(income)
    db.commit()
    db.refresh(income)
    return income


@router.get("/{income_id}", response_model=IncomeRead)
def get_income(income_id: IncomeId, db: DbSession) -> Income:
    return _get_or_404(db, income_id)


@router.patch("/{income_id}", response_model=IncomeRead)
def update_income(
    income_id: IncomeId,
    payload: IncomeUpdate,
    db: DbSession,
) -> Income:
    income = _get_or_404(db, income_id)
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(income, field, value)
    db.commit()
    db.refresh(income)
    return income


@router.delete("/{income_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_income(income_id: IncomeId, db: DbSession) -> None:
    income = _get_or_404(db, income_id)
    db.delete(income)
    db.commit()

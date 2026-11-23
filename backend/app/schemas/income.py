from datetime import date, datetime
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, model_validator

Amount = Annotated[Decimal, Field(gt=0, max_digits=12, decimal_places=2)]
Source = Annotated[str, Field(min_length=1, max_length=100)]
Currency = Annotated[str, Field(pattern=r"^[A-Z]{3}$")]
Notes = Annotated[str, Field(max_length=500)]


class IncomeBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")


class IncomeCreate(IncomeBase):
    source: Source
    amount: Amount
    currency: Currency = "ZAR"
    received_on: date
    notes: Notes | None = None


class IncomeUpdate(IncomeBase):
    source: Source | None = None
    amount: Amount | None = None
    currency: Currency | None = None
    received_on: date | None = None
    notes: Notes | None = None

    @model_validator(mode="after")
    def reject_null_required_fields(self) -> "IncomeUpdate":
        for name in ("source", "amount", "currency", "received_on"):
            if name in self.model_fields_set and getattr(self, name) is None:
                raise ValueError(f"{name} cannot be set to null")
        return self


class IncomeRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    source: str
    amount: Decimal
    currency: str
    received_on: date
    notes: str | None
    created_at: datetime
    updated_at: datetime

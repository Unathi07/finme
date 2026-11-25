# Adding the Income model
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import CheckConstraint, Date, DateTime, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Income(Base):
    __tablename__ = "income"
    __table_args__ = (
        CheckConstraint(
            "amount > 0",
            name="ck_income_amount_positive",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)  # int col for ID
    source: Mapped[str] = mapped_column(
        String(100)
    )  # where the money is from (Salary, allowance, etc.)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))  # decimal amount of the money
    currency: Mapped[str] = mapped_column(
        String(3), default="ZAR", server_default="ZAR"
    )  # ZAR currency
    received_on: Mapped[date] = mapped_column(Date, index=True)  # date it was recieved
    notes: Mapped[str | None] = mapped_column(
        String(500)
    )  # Free text to provide further context for the income(Optional)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )  # time satmp with the timezone
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

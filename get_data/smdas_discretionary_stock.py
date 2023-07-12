from sqlalchemy import TEXT, BIGINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# class the table
class Base(DeclarativeBase):
    pass


class DiscretionaryStock(Base):
    __tablename__ = 'discretionary_stock'
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    account: Mapped[str] = mapped_column(TEXT)
    stock_code: Mapped[str] = mapped_column(TEXT)


class PersonalityModule(Base):
    __tablename__ = 'discretionary_stock'
    id = mapped_column(BIGINT, primary_key=True)
    account: Mapped[str] = mapped_column(TEXT)
    preference: Mapped[str] = mapped_column(TEXT)
    prediction: Mapped[str] = mapped_column(TEXT)
    history: Mapped[str] = mapped_column(TEXT)

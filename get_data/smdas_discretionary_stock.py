from sqlalchemy import Column, TEXT, BIGINT
from sqlalchemy.orm import DeclarativeBase


# class the table
class Base(DeclarativeBase):
    pass


class DiscretionaryStock(Base):
    __tablename__ = "discretionary_stock"
    id = Column(BIGINT, primary_key=True)
    account = Column(TEXT)
    stock_code = Column(TEXT)


class PersonalityModule(Base):
    __tablename__ = "discretionary_stock"
    id = Column(BIGINT, primary_key=True)
    account = Column(TEXT)
    preference = Column(TEXT)
    prediction = Column(TEXT)
    history = Column(TEXT)

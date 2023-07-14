from datetime import date

from sqlalchemy import BIGINT, TEXT, DATE, DECIMAL, INT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class CompanyShareholderInfo(Base):
    __tablename__ = "company_shareholder_info"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    stock_code: Mapped[str] = mapped_column(TEXT)
    rank: Mapped[int] = mapped_column(INT)
    name: Mapped[str] = mapped_column(TEXT)
    identity: Mapped[str] = mapped_column(TEXT)
    counting: Mapped[int] = mapped_column(BIGINT)
    rate: Mapped[str] = mapped_column(DECIMAL)
    change_count: Mapped[int] = mapped_column(BIGINT)
    change_percentage: Mapped[str] = mapped_column(DECIMAL)


class DailyNewsUrl(Base):
    __tablename__ = "daily_news_url"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    link: Mapped[str] = mapped_column(TEXT)
    title: Mapped[str] = mapped_column(TEXT)
    date: Mapped[str] = mapped_column(DATE)


class KlineGraph(Base):
    __tablename__ = "kline_graph"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    stock_code: Mapped[str] = mapped_column(TEXT)
    date: Mapped[date] = mapped_column(DATE)
    total_amount: Mapped[int] = mapped_column(BIGINT)
    total_sales: Mapped[float] = mapped_column(DECIMAL)
    open_price: Mapped[float] = mapped_column(DECIMAL)
    close_price: Mapped[float] = mapped_column(DECIMAL)
    highest_price: Mapped[float] = mapped_column(DECIMAL)
    lowest_price: Mapped[float] = mapped_column(DECIMAL)
    increase: Mapped[float] = mapped_column(DECIMAL)

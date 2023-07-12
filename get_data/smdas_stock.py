from datetime import date

from sqlalchemy import BIGINT, TEXT, DATE, DECIMAL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase()):
    pass


# class the table
class CompanyBasicInfo(Base):
    __tablename__ = 'company_basic_info'
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    stock_code: Mapped[str] = mapped_column(TEXT)
    name: Mapped[str] = mapped_column(TEXT)
    intro: Mapped[str] = mapped_column(TEXT)
    leader: Mapped[str] = mapped_column(TEXT)
    distribution: Mapped[str] = mapped_column(TEXT)
    notice: Mapped[str] = mapped_column(TEXT)


class CompanyFinancialInfo(Base):
    __tablename__ = 'company_financial_info'
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    stock_code: Mapped[str] = mapped_column(TEXT)
    property: Mapped[float] = mapped_column(DECIMAL)
    liability: Mapped[float] = mapped_column(DECIMAL)
    interest: Mapped[float] = mapped_column(DECIMAL)
    income: Mapped[float] = mapped_column(DECIMAL)
    profit: Mapped[float] = mapped_column(DECIMAL)
    asset_turnover: Mapped[float] = mapped_column(DECIMAL)
    account_receivable_turnover: Mapped[float] = mapped_column(DECIMAL)
    inventory_turnover: Mapped[float] = mapped_column(DECIMAL)
    operating_cycle: Mapped[float] = mapped_column(DECIMAL)


class CompanyShareholderInfo(Base):
    __tablename__ = 'company_shareholder_info'
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    stock_code: Mapped[str] = mapped_column(TEXT)
    name: Mapped[str] = mapped_column(TEXT)
    identity: Mapped[str] = mapped_column(TEXT)
    counting: Mapped[int] = mapped_column(BIGINT)
    rate: Mapped[str] = mapped_column(DECIMAL)
    period: Mapped[str] = mapped_column(DATE)


class DailyNewsUrl(Base):
    __tablename__ = 'daily_news_url'
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    url: Mapped[str] = mapped_column(TEXT)
    title: Mapped[str] = mapped_column(TEXT)
    intro: Mapped[str] = mapped_column(TEXT)
    cover: Mapped[str] = mapped_column(TEXT)


class KlineGraph(Base):
    __tablename__ = 'kline_graph'
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    stock_code: Mapped[str] = mapped_column(TEXT)
    date: Mapped[date] = mapped_column(DATE)
    total_amount: Mapped[int] = mapped_column(BIGINT)
    total_sales: Mapped[float] = mapped_column(DECIMAL)
    average_price: Mapped[float] = mapped_column(DECIMAL)
    open_price: Mapped[float] = mapped_column(DECIMAL)
    close_price: Mapped[float] = mapped_column(DECIMAL)
    highest_price: Mapped[float] = mapped_column(DECIMAL)
    lowest_price: Mapped[float] = mapped_column(DECIMAL)
    increase: Mapped[float] = mapped_column(DECIMAL)


class TransactionDataSeparate(Base):
    __tablename__ = 'transaction_data_separate'
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    stock_code: Mapped[str] = mapped_column(TEXT)
    date: Mapped[date] = mapped_column(DATE)
    amount: Mapped[int] = mapped_column(BIGINT)
    price: Mapped[float] = mapped_column(DECIMAL)

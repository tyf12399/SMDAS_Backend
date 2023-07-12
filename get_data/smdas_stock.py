from sqlalchemy import Column, BIGINT, TEXT, DATE, DECIMAL
from sqlalchemy.orm import declarative_base


class Base(declarative_base()):
    pass


# class the table
class CompanyBasicInfo(Base):
    __tablename__ = "company_basic_info"
    id = Column(BIGINT, primary_key=True)
    stock_code = Column(TEXT)
    name = Column(TEXT)
    intro = Column(TEXT)
    leader = Column(TEXT)
    distribution = Column(TEXT)
    notice = Column(TEXT)


class CompanyFinancialInfo(Base):
    __tablename__ = "company_financial_info"
    id = Column(BIGINT, primary_key=True)
    stock_code = Column(TEXT)
    property = Column(DECIMAL)
    liability = Column(DECIMAL)
    interest = Column(DECIMAL)
    income = Column(DECIMAL)
    profit = Column(DECIMAL)
    asset_turnover = Column(DECIMAL)
    account_receivable_turnover = Column(DECIMAL)
    inventory_turnover = Column(DECIMAL)
    operating_cycle = Column(DECIMAL)


class CompanyShareholderInfo(Base):
    __tablename__ = "company_shareholder_info"
    id = Column(BIGINT, primary_key=True)
    stock_code = Column(TEXT)
    name = Column(TEXT)
    identity = Column(TEXT)
    counting = Column(BIGINT)
    rate = Column(DECIMAL)
    period = Column(DATE)


class DailyNewsUrl(Base):
    __tablename__ = "daily_news_url"
    id = Column(BIGINT, primary_key=True)
    url = Column(TEXT)
    title = Column(TEXT)
    intro = Column(TEXT)
    cover = Column(TEXT)


class KlineGraph(Base):
    __tablename__ = "kline_graph"
    id = Column(BIGINT, primary_key=True)
    stock_code = Column(TEXT)
    date = Column(DATE)
    total_amount = Column(BIGINT)
    total_sales = Column(DECIMAL)
    average_price = Column(DECIMAL)
    open_price = Column(DECIMAL)
    close_price = Column(DECIMAL)
    highest_price = Column(DECIMAL)
    lowest_price = Column(DECIMAL)
    increase = Column(DECIMAL)


class TransactionDataSeparate(Base):
    __tablename__ = "transaction_data_separate"
    id = Column(BIGINT, primary_key=True)
    stock_code = Column(TEXT)
    date = Column(DATE)
    amount = Column(BIGINT)
    price = Column(DECIMAL)

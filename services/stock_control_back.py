from datetime import datetime

from dotenv import dotenv_values
from sqlalchemy import create_engine, select, update, delete, and_
from sqlalchemy.orm import Session

from get_data.smdas_stock import CompanyShareholderInfo
from get_data.smdas_stock import KlineGraph, DailyNewsUrl

config = dotenv_values(".env")

host = config["host"]
port = config["port"]
user = config["user"]
passwd = config["passwd"]
db = config["db2"]
connect_timeout = config["connect_timeout"]

db_url = "".join(
    [
        "mariadb+mariadbconnector://",
        user,
        ":",
        passwd,
        "@",
        host,
        ":",
        port,
        "/",
        db,
        "?charset=utf8",
    ]
)
engine = create_engine(db_url)


# update the record
def update_company_shareholder_info(
    stock_code: int,
    name: str,
    rank: int = None,
    identity: str = None,
    counting: int = None,
    rate: float = None,
    change_count: int = None,
    change_percentage: float = None,
):
    with engine.begin() as session:
        prep = (
            update(CompanyShareholderInfo)
            .where(CompanyShareholderInfo.stock_code == stock_code)
            .where(CompanyShareholderInfo.name == name)
            .values(rank=rank)
            .values(identity=identity)
            .values(counting=counting)
            .values(rate=rate)
            .values(change_count=change_count)
            .values(change_percentage=change_percentage)
        )
        session.execute(prep)


def update_kline_graph_info(
    stock_code: str,
    date: str,
    total_amount: str = None,
    total_sales4: str = None,
    open_price4: str = None,
    close_price4: str = None,
    highest_price4: str = None,
    lowest_price4: str = None,
    increase4: str = None,
):
    with engine.begin() as session:
        prep = (
            update(KlineGraph)
            .where(KlineGraph.stock_code == stock_code, KlineGraph.date == date)
            .values(total_amount=total_amount)
            .values(total_sales=total_sales4)
            .values(open_price=open_price4)
            .values(close_price=close_price4)
            .values(highest_price=highest_price4)
            .values(lowest_price=lowest_price4)
            .values(increase=increase4)
        )
        session.execute(prep)


def delete_company_shareholder_info(stock_code3: str, name3: str):
    with engine.begin() as session:
        prep = (
            delete(CompanyShareholderInfo)
            .where(CompanyShareholderInfo.stock_code == stock_code3)
            .where(CompanyShareholderInfo.name == name3)
        )
        session.execute(prep)


def delete_kline_graph_info(stock_code5: str, date5: str):
    with Session(engine) as session:
        prep = (
            delete(KlineGraph)
            .where(KlineGraph.stock_code == stock_code5)
            .where(KlineGraph.date == date5)
        )
        session.execute(prep)


def company_shareholder_info_query(stock_code: str = None, name: str = None):
    with Session(engine) as session:
        stmt = select(CompanyShareholderInfo)
        # 构建查询条件
        conditions = []
        if stock_code is not None or stock_code == "":
            stock_code = int(stock_code)
            conditions.append(CompanyShareholderInfo.stock_code == stock_code)
        if name is not None:
            conditions.append(CompanyShareholderInfo.name == name)

        if conditions:
            stmt = stmt.where(and_(*conditions)).limit(1000)

        result = session.execute(stmt).all()
        result = [
            {
                "account": item[0].id,
                "stock_code": item[0].stock_code,
                "rank": item[0].rank,
                "name": item[0].name,
                "identity": item[0].identity,
                "counting": item[0].counting,
                "rate": float(item[0].rate),
                "change_count": item[0].change_count,
                "change_percentage": str(item[0].change_percentage),
            }
            for item in result
        ]
        return result


def kline_graph_query(
    stock_code: str = None, date_start: str = None, date_end: str = None
):
    with Session(engine) as session:
        stmt = select(KlineGraph)

        conditions = []
        if stock_code is not None:
            conditions.append(KlineGraph.stock_code == stock_code)
        if date_start is not None:
            conditions.append(KlineGraph.date >= date_start)
        if date_end is not None:
            conditions.append(KlineGraph.date <= date_end)

        if conditions:
            stmt = stmt.where(and_(*conditions)).limit(1000)

        result = session.execute(stmt).all()
        result = [
            {
                "stock_code": item[0].stock_code,
                "date": item[0].date,
                "total_amount": item[0].total_amount,
                "total_sales": item[0].total_sales,
                "average_price": item[0].total_sales / item[0].total_amount,
                "open_price": item[0].open_price,
                "close_price": item[0].close_price,
                "highest_price": item[0].highest_price,
                "lowest_price": item[0].lowest_price,
                "increase": item[0].increase,
                "account": item[0].id,
            }
            for item in result
        ]
        return result


def daily_news_query(date_start: str = None, date_end: str = None):
    with Session(engine) as session:
        stmt = select(DailyNewsUrl)

        conditions = []
        if date_start is not None:
            conditions.append(DailyNewsUrl.date >= date_start)
        if date_end is not None:
            conditions.append(DailyNewsUrl.date <= date_end)

        if conditions:
            stmt = stmt.where(and_(*conditions)).limit(1000)

        result = session.execute(stmt).all()
        result = [
            {
                "id": item[0].title,
                "title": item[0].title,
                "link": item[0].link,
                "date": item[0].date,
            }
            for item in result
        ]
        return result

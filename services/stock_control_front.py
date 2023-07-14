from dotenv import dotenv_values
from dotenv import dotenv_values
from sqlalchemy import create_engine, select, and_
from sqlalchemy.orm import Session

from get_data.smdas_stock import KlineGraph

from datetime import datetime

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


# create the kline graph
def select_kline_graph(stock_code: str):
    with Session(engine) as session:
        stmt = select(KlineGraph)
        # query condition
        conditions = []
        conditions.append(KlineGraph.stock_code == stock_code)
        conditions.append(KlineGraph.date > "2023-06-07")
        stmt = stmt.where(and_(*conditions))

        result = session.execute(stmt).all()
        result = [
            {
                "date": item[0].date,
                "openprice": item[0].open_price,
                "closeprice": item[0].close_price,
                "highprice": item[0].highest_price,
                "lowprice": item[0].lowest_price,
            }
            for item in result
        ]
        return result


def sh_stock_list():
    with Session(engine) as session:
        stmt = select(KlineGraph)

        # query condition
        conditions = []
        conditions.append(KlineGraph.stock_code > 599999)
        conditions.append(KlineGraph.date == "2023-07-07")

        stmt = stmt.where(and_(*conditions))

        result = session.execute(stmt).all()

        result = [
            {
                "hustock": item[0].stock_code,
                "hudate": "2023-07-07",
                "huamount": item[0].total_amount,
                "husales": item[0].total_sales,
                "huprice": item[0].total_sales / item[0].total_amount,
                "huopenprice": item[0].open_price,
                "hucloseprice": item[0].close_price,
                "huhighprice": item[0].highest_price,
                "hulowprice": item[0].lowest_price,
                "huincrease": item[0].increase,
            }
            for item in result
        ]
        return result


def sz_stock_list():
    with Session(engine) as session:
        stmt = select(KlineGraph)

        # query condition
        conditions = []
        conditions.append(KlineGraph.stock_code < 600000)
        conditions.append(KlineGraph.date == "2023-07-07")

        stmt = stmt.where(and_(*conditions))

        result = session.execute(stmt).all()

        result = [
            {
                "shenstock": item[0].stock_code,
                "shendate": "2023-07-07",
                "shenamount": item[0].total_amount,
                "shensales": item[0].total_sales,
                "shenprice": item[0].total_sales / item[0].total_amount,
                "shenopenprice": item[0].open_price,
                "shencloseprice": item[0].close_price,
                "shenhighprice": item[0].highest_price,
                "shenlowprice": item[0].lowest_price,
                "shenincrease": item[0].increase,
            }
            for item in result
        ]
        return result

def his_record(code):
    with Session(engine) as session:
        stmt = select(KlineGraph)

        # query condition
        conditions = []
        conditions.append(KlineGraph.stock_code == code)

        stmt = stmt.where(and_(*conditions))

        result = session.execute(stmt).all()

        result = [
            {
                "hisstockid": item[0].stock_code,
                "hisdate": "2023-07-07",
                "hisamount": item[0].total_amount,
                "hissales": item[0].total_sales,
                "hisprice": item[0].total_sales / item[0].total_amount,
                "hisopenprice": item[0].open_price,
                "hiscloseprice": item[0].close_price,
                "hishighprice": item[0].highest_price,
                "hislowprice": item[0].lowest_price,
                "hisincrease": item[0].increase,
            }
            for item in result
        ]
        return result
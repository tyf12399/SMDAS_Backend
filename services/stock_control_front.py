import numpy as np
import pandas as pd
from dotenv import dotenv_values
from sqlalchemy import create_engine, select, update, delete
from sqlalchemy.orm import Session

from get_data.smdas_stock import CompanyBasicInfo, CompanyFinancialInfo, CompanyShareholderInfo
from get_data.smdas_stock import DailyNewsUrl, KlineGraph, TransactionDataSeparate

config = dotenv_values("../.env")

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
def select_kline_graph(stock_code, date):
    with Session(engine) as session:
        kline = select(KlineGraph).where(KlineGraph.stock_code.in_(stock_code))\
            .where(KlineGraph.date.in_(date))
        return kline

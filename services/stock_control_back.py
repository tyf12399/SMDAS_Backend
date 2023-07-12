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


# data insert
def insert_data_to_kline_graph(csv_file_path):
    dtype = {
        'open_price': np.float64, 'stock_code': np.string_,
        'close_price': np.float64, 'highest_price': np.float64,
        'lowest_price': np.float64, 'total_amount': np.float64,
        'total_sales': np.float64, 'increase': np.float64,
    }
    data = pd.read_csv('../sh_kline.csv', dtype=dtype, engine='python')
    data.to_sql('kline_graph', engine, if_exists='append', index=False)


# create the record
def create_company_basic_info(stock_code1, name1, intro1, leader1, distribution1, notice1):
    with Session(engine) as session:
        basic = CompanyBasicInfo(
            stock_code=stock_code1, name=name1, intro=intro1, leader=leader1,
            distribution=distribution1, notice=notice1
        )
        session.add(basic)
        session.commit()


def create_company_financial_info(stock_code2, property2, liability2, interest2, income2, profit2,
                                  asset_turnover2, account_receivable_turnover2, inventory_turnover2,
                                  operating_cycle2):
    with Session(engine) as session:
        financial = CompanyFinancialInfo(
            stock_code=stock_code2, property=property2, liability=liability2,
            interest=interest2, income=income2, profit=profit2, asset_turnover=asset_turnover2,
            account_receivable_turnover=account_receivable_turnover2,
            inventory_turnover=inventory_turnover2, operating_cycle=operating_cycle2
        )
        session.add(financial)
        session.commit()


def create_company_shareholder_info(stock_code3, name3, identity3, counting3, rate3, period3):
    with Session(engine) as session:
        shareholder = CompanyShareholderInfo(
            stock_code=stock_code3, name=name3, identity=identity3,
            counting=counting3, rate=rate3, period=period3
        )
        session.add(shareholder)
        session.commit()


def create_kline_graph(stock_code5, date5, open_price5, close_price5, highest_price5, lowest_price5,
                       total_amount5, total_sales5, increase5):
    with Session(engine) as session:
        kline = KlineGraph(
            stock_code=stock_code5, date=date5, open_price=open_price5, close_price=close_price5,
            highest_price=highest_price5, lowest_price=lowest_price5, total_amount=total_amount5,
            total_sales=total_sales5, increase=increase5
        )
        session.add(kline)
        session.commit()


def create_transaction_data_separate(stock_code6, date6, amount6, price6):
    with Session(engine) as session:
        transaction = TransactionDataSeparate(
            stock_code=stock_code6, date=date6, amount=amount6, price=price6
        )
        session.add(transaction)
        session.commit()


# update the record
def update_company_basic_info(stock_code1, intro1, leader1, distribution1, notice1):
    with Session() as session:
        prep = (
            update(CompanyBasicInfo).where(CompanyBasicInfo.stock_code.in_(stock_code1))
            .values(intro=intro1)
            .values(leader=leader1)
            .values(distribution=distribution1)
            .values(notice=notice1)
        )
        session.execute(prep)


def update_company_financial_info(stock_code2, property2, liability2, interest2, income2,
                                  profit2, asset_turnover2, account_receivable_turnover2,
                                  inventory_turnover2, operating_cycle2):
    with Session() as session:
        prep = (
            update(CompanyFinancialInfo).where(CompanyFinancialInfo.stock_code.in_(stock_code2))
            .values(property=property2)
            .values(liability=liability2)
            .values(interest=interest2)
            .values(income=income2)
            .values(profit=profit2)
            .values(asset_turnover=asset_turnover2)
            .values(account_receivable_turnover=account_receivable_turnover2)
            .values(inventory_turnover=inventory_turnover2)
            .values(operating_cycle=operating_cycle2)
        )
        session.execute(prep)


def update_company_shareholder_info(stock_code3, name3, identity3, counting3, rate3, period3):
    with Session() as session:
        prep = (
            update(CompanyShareholderInfo).where(CompanyShareholderInfo.stock_code.in_(stock_code3),
                                                 CompanyShareholderInfo.name.in_(name3))
            .values(identity=identity3)
            .values(counting=counting3)
            .values(rate=rate3)
            .values(period=period3)
        )
        session.execute(prep)


def update_kline_graph_info(stock_code4, date4, total_amount4, total_sales4,
                            average_price4, open_price4, close_price4,
                            highest_price4, lowest_price4, increase4):
    with Session() as session:
        prep = (
            update(KlineGraph).where(KlineGraph.stock_code.in_(stock_code4), KlineGraph.date.in_(date4))
            .values(total_amount=total_amount4)
            .values(total_sales=total_sales4)
            .values(average_price=average_price4)
            .values(open_price=open_price4)
            .values(close_price=close_price4)
            .values(highest_price=highest_price4)
            .values(lowest_price=lowest_price4)
            .values(increase=increase4)
        )
        session.execute(prep)


def update_transaction_data_separate(id5, stock_code5, date5, amount5, price5):
    with Session() as session:
        prep = (
            update(TransactionDataSeparate).where(KlineGraph.id.in_(id5))
            .values(stock_code=stock_code5)
            .values(date=date5)
            .values(amount=amount5)
            .values(price=price5)
        )
        session.execute(prep)


# delete the record
def delete_company_basic_info(stock_code1):
    with Session() as session:
        prep = (delete(CompanyBasicInfo).where(CompanyBasicInfo.stock_code.in_(stock_code1)))
        session.execute(prep)


def delete_company_financial_info(stock_code2):
    with Session() as session:
        prep = (delete(CompanyFinancialInfo).where(CompanyFinancialInfo.stock_code.in_(stock_code2)))
        session.execute(prep)


def delete_company_shareholder_info(stock_code3, name3):
    with Session() as session:
        prep = (
            delete(CompanyShareholderInfo)
            .where(CompanyShareholderInfo.stock_code.in_(stock_code3))
            .where(CompanyShareholderInfo.name.in_(name3))
        )
        session.execute(prep)


def delete_kline_graph_info(stock_code5, date5):
    with Session() as session:
        prep = (delete(KlineGraph)
                .where(KlineGraph.stock_code.in_(stock_code5))
                .where(KlineGraph.date.in_(date5))
                )
        session.execute(prep)


def delete_transaction_data_separate(stock_code6, date6, amount6, price6):
    with Session() as session:
        prep = (delete(TransactionDataSeparate)
                .where(TransactionDataSeparate.stock_code.in_(stock_code6))
                .where(TransactionDataSeparate.date.in_(date6))
                .where(TransactionDataSeparate.amount.in_(amount6))
                .where(TransactionDataSeparate.price.in_(price6))
                )
        session.execute(prep)


# basic query
def select_basic_info(stock_code, name):
    with Session() as session:
        basic = select(CompanyBasicInfo).where(CompanyBasicInfo.stock_code.in_([stock_code])). \
            where(CompanyBasicInfo.name.in_([name]))
        return basic


def company_financial_info_query(stock_code, inventory_turnover):
    with Session() as session:
        financial = select(CompanyFinancialInfo).where(CompanyFinancialInfo.stock_code.in_([stock_code])) \
            .where(CompanyFinancialInfo.inventory_turnover.in_(inventory_turnover))
        return financial


def company_shareholder_info_query(stock_code, name):
    with Session() as session:
        shareholder = select(CompanyShareholderInfo).where(CompanyShareholderInfo.stock_code.in_([stock_code])) \
            .where(CompanyShareholderInfo.name.in_(name))
        return shareholder


def kline_graph_query(stock_code, date_start, date_end):
    with Session() as session:
        kline = select(KlineGraph).where(KlineGraph.stock_code.in_(stock_code))\
            .where(KlineGraph.date>=date_start)\
            .where(KlineGraph.date<=date_end)
        return kline


def transaction_data_separate_query(stock_code, date_start, date_end):
    with Session() as session:
        transaction = select(TransactionDataSeparate).where(TransactionDataSeparate.stock_code.in_([stock_code])) \
            .where(TransactionDataSeparate.date>=date_start) \
            .where(TransactionDataSeparate.date<=date_end)
        return transaction

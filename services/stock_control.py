import numpy as np
import pandas as pd
from dotenv import dotenv_values
from sqlalchemy import create_engine
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


def create_daily_news_url(url4, title4, intro4, cover4):
    with Session(engine) as session:
        dailynews = DailyNewsUrl(
            url=url4, title=title4, intro=intro4, cover=cover4
        )
        session.add(dailynews)
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


def create_transaction_data_seperate(stock_code6, date6, amount6, price6):
    with Session(engine) as session:
        transaction = TransactionDataSeparate(
            stock_code=stock_code6, date=date6, amount=amount6, price=price6
        )
        session.add(transaction)
        session.commit()


# modify the record
def modify_company_basic_info(keyword, condition, Target):
    with Session() as session:
        basic = Session.query(company_basic_info).filter_by(company_basic_info.keyword == condition).first()
        basic.attribute = Target
        Session.commit()


def modify_company_financial_info(keyword, contidion, Target):
    with Session() as session:
        financial = Session.query(company_financial_info).filter_by(
            company_financial_info.keyword == contidion).first()
        financial.attribute = Target
        Session.commit()


def modify_company_shaerholder_info(keyword, condition, Target):
    with Session() as session:
        shareholder = Session.query(company_shareholder_info).filter_by(
            company_shareholder_info.keyword == condition).first()
        shareholder.attribute = Target
        Session.commit()


def modify_daily_news_url(keyword, condition, Target):
    with Session() as session:
        dailynews = Session.query(daily_news_url).filter_by(daily_news_url.keyword == condition).first()
        dailynews.attribute = Target
        Session.commit()


def modify_kline_graph_info(keyword, condition, Target):
    with Session() as session:
        kline = Session.query(kline_graph).filter_by(kline_graph_info.keyword == condition).first()
        kline.attribute = Target
        Session.commit()


def modify_transaction_data_seperate(keyword, condition, Target):
    with Session() as session:
        transaction = Session.query(transaction_data_seperate).filter_by(
            transaction_data_seperate.keyword == condition).first()
        transaction.attribute = Target
        Session.commit()


# delete the record
def delete_company_basic_info(keyword, condition):
    with Session() as session:
        basic = Session.query(company_basic_info).filter_by(compamy_basic_info.keyword == condition).first()
        Session.delete(Basic)
        Session.commit()


def delete_company_financial_info(keyword, condition):
    with Session() as session:
        financial = Session.query(company_financial_info).filter_by(
            company_fiancial_info.keyword == condition).first()
        Session.delete(Financial)
        Session.commit()


def delete_company_shaerholder_info(keyword, condition):
    with Session() as session:
        shareholder = Session.query(company_shareholder_info).filter_by(
            company_shareholder_info.keyword == condition).first()
        Session.delete(Shareholder)
        Session.commit()


def delete_daily_news_url(keyword, condition):
    with Session() as session:
        dailynews = Session.query(daily_news_url).filter_by(daily_news_url.keyword == condition).first()
        Session.delete(dailynews)
        Session.commit()


def delete_kline_graph_info(keyword, condition):
    with Session() as session:
        kline = Session.query(kline_graph).filter_by(kline_graph.keyword == condition).first()
        Session.delete(Kline)
        Session.commit()


def delete_transaction_data_seperate(keyword, condition):
    with Session() as session:
        transaction = Session.query(transaction_data_seperate).filter_by(
            transaction_data_seperate.keyword == condition).first()
        Session.delete(Transaction)
        Session.commit()


# basic query
def company_basic_info_query(keyword, condition):
    with Session() as session:
        basic = Session.query(company_basic_info).filter(company_basic_info.keyword == condition).all()
        data = [dict(zip(basic.keys(), basic)) for result in basic]


def company_financial_info_query(keyword, condition):
    with Session() as session:
        financial = Session.query(company_financial_info).filter(company_financial_info.keyword == condition).all()
        data = [dict(zip(financial.keys(), financial)) for result in financial]


def company_shareholder_info_query(keyword, condition):
    with Session() as session:
        shareholder = Session.query(company_shareholder_info).filter(
            company_shareholder_info.keyword == condition).all()
        data = [dict(zip(shareholder.keys(), shareholder)) for result in shareholder]


def daily_news_url_query(keyword, condition):
    with Session() as session:
        dailynews = Session.query(daily_news_url).filter(daily_news_url.keyword == condition).all()
        data = [dict(zip(dailynews.keys(), dailynews)) for result in dailynews]


def kline_graph_query(keyword, condition):
    with Session() as session:
        kline = Session.query(kline_graph).filter(kline_graph.keyword == condition).all()
        data = [dict(zip(kline.keys(), kline)) for result in kline]


def transaction_data_seperate_query(keyword, condition):
    with Session() as session:
        transaction = Session.query(transaction_data_seperate).filter(
            transaction_data_seperate.keyword == condition).all()
        data = [dict(zip(transaction.keys(), transaction)) for result in transaction]

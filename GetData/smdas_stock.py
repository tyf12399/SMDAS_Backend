import datetime
import numpy as np
import os
import pandas as pd
import pymysql
import requests
from dotenv import dotenv_values
from lxml import etree
from sqlalchemy import Column, Integer, String, Text, ForeignKey, FLOAT, Date
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy.orm import column_property, relationship, deferred
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

class SmdasStock:

    def __init__(self):
        config = dotenv_values(".env")
        host = config["host"]
        port = config["port"]
        user = config["user"]
        passwd = config["passwd"]
        db = config["db2"]
        connect_timeout = config["connect_timeout"]

        db_url = "".join(["mysql+pymysql://", user, ":", passwd, "@", host, ":", port, "/", db, "?charset=utf8"])
        self.engine = create_engine(db_url)
        self.Base = declarative_base()

        Session = sessionmaker(bind = self.engine)
        self.session = Session()

    def table_create(self):
    # class the table
        class company_basic_info(self.Base):
            __tablename__ = 'company_basic_info'
            id = Column(Integer, primary_key=True)
            stock_code = Column(String)
            name = Column(String)
            intro = Column(String)
            leader = Column(String)
            distribution = Column(String)
            notice = Column(String)


        class company_financial_info(self.Base):
            __tablename__ = 'company_financial_info'
            id = Column(Integer, primary_key=True)
            stock_code = Column(String)
            property = Column(FLOAT)
            liability = Column(FLOAT)
            interest = Column(FLOAT)
            income = Column(FLOAT)
            profit = Column(FLOAT)
            asset_turnover = Column(FLOAT)
            account_receivable_turnover = Column(FLOAT)
            inventory_turnover = Column(FLOAT)
            operating_cycle = Column(FLOAT)


        class company_shareholder_info(self.Base):
            __tablename__ = 'company_shareholder_info'
            id = Column(Integer, primary_key=True)
            stock_code = Column(String)
            name = Column(String)
            identity = Column(String)
            counting = Column(Integer)
            rate = Column(FLOAT)
            period = Column(Date)

        class daily_news_url(self.Base):
            __tablename__ = 'daily_news_url'
            id = Column(Integer, primary_key=True)
            url = Column(String)
            title = Column(String)
            intro = Column(String)
            cover = Column(String)


        class kline_graph(self.Base):
            __tablename__ = 'kline_graph'
            id = Column(Integer, primary_key=True)
            stock_code = Column(String)
            date = Column(Date)
            total_amount = Column(Integer)
            total_sales = Column(FLOAT)
            average_price = Column(FLOAT)
            open_price = Column(FLOAT)
            close_price = Column(FLOAT)
            highest_price = Column(FLOAT)
            lowest_price = Column(FLOAT)
            increase = Column(FLOAT)


        class transaction_data_seperate(self.Base):
            __tablename__ = 'transaction_data_seperate'
            id = Column(Integer, primary_key=True)
            stock_code = Column(String)
            date = Column(Date)
            amount = Column(Integer)
            price = Column(FLOAT)


    def data_insert(self):
        def insert_data_to_kline_graph(self, csv_file_path):
            dtype = {
                'open_price': np.float64, 'stock_code': np.string_,
                'close_price': np.float64, 'highest_price': np.float64,
                'lowest_price': np.float64, 'total_amount': np.float64,
                'total_sales': np.float64, 'increase': np.float64,
            }
            data = pd.read_csv('../sh_kline.csv', dtype=dtype, engine='python')
            data.to_sql('kline_graph', engine, if_exists='append', index=False)


    # create the record
    def record_create(self):
        def create_company_basic_info(self, stock_code1, name1, intro1, leader1, distribution1, notice1):
            basic = company_basic_info(
                stock_code = stock_code1, name = name1, intro = intro1, leader = leader1,
                distribution = distribution1, notice = notice1
            )
            Session.add(basic)
            Session.commit()


        def create_company_financial_info(self, stock_code2, property2, liability2, interest2, income2, profit2, asset_turnover2, account_receivable_turnover2, inventory_turnover2, operating_cycle2):
            financial = company_financial_info(
                stock_code = stock_code2, property = property2, liability = liability2,
                interest = interest2, income = income2, profit = profit2, asset_turnover = asset_turnover2,
                account_receivable_turnover = account_receivable_turnover2,
                inventory_turnover = inventory_turnover2, operating_cycle = operating_cycle2
            )
            Session.add(financial)
            Session.commit()

        def create_company_shareholder_info(self, stock_code3, name3, identity3, counting3, rate3, period3):
            shareholder = company_shareholder_info(
                stock_code = stock_code3, name = name3, identity = identity3,
                counting = counting3, rate = rate3, period = period3
            )
            Session.add(shareholder)
            Session.commit()

        def create_daily_news_url(self, url4, title4, intro4, cover4):
            dailynews = company_shareholder_info(
                url = url4, title = title4, intro = intro4, cover = cover4
            )
            Session.add(dailynews)
            Session.commit()
        def create_kline_graph(self, stock_code5, date5, open_price5, close_price5, highest_price5, lowest_price5, total_amount5, total_sales5, increase5):
           kline = kline_graph(
               stock_code = stock_code5, date = date5, open_price = open_price5, close_price = close_price5,
               highest_price = highest_price5, lowest_price = lowest_price5, total_amount = total_amount5,
               total_sales = total_sales5, increase = increase5
           )
           Session.add(kline)
           Session.commit()

        def create_transaction_data_seperate(self, stock_code6, date6, amount6, price6):
            transaction = transaction_data_seperate(
                stock_code = stock_code6, date = date6, amount = amount6, price = price6
            )
            Session.add(transaction)
            Session.commit()


    def record_modify(self):
        # #modify the record
        def modify_company_basic_info(self, keyword, condition, Target):
            with Session() as session:
                basic = Session.query(company_basic_info).filter_by(company_basic_info.keyword == condition).first()
                basic.attribute = Target
                Session.commit()

        def modify_company_financial_info(self, keyword, contidion, Target):
            with Session() as session:
                financial = Session.query(company_financial_info).filter_by(company_financial_info.keyword == contidion).first()
                financial.attribute = Target
                Session.commit()

        def modify_company_shaerholder_info(self, keyword, condition, Target):
            with Session() as session:
                shareholder = Session.query(company_shareholder_info).filter_by(company_shareholder_info.keyword == condition).first()
                shareholder.attribute = Target
                Session.commit()

        def modify_daily_news_url(self, keyword, condition, Target):
            with Session() as session:
                dailynews = Session.query(daily_news_url).filter_by(daily_news_url.keyword == condition).first()
                dailynews.attribute = Target
                Session.commit()

        def modify_kline_graph_info(self, keyword, condition, Target):
            with Session() as session:
                kline = Session.query(kline_graph).filter_by(kline_graph_info.keyword == condition).first()
                kline.attribute = Target
                Session.commit()

        def modify_transaction_data_seperate(self, keyword, condition, Target):
            with Session() as session:
                transaction = Session.query(transaction_data_seperate).filter_by(transaction_data_seperate.keyword == condition).first()
                transaction.attribute = Target
                Session.commit()

    def record_delete(self):
        #delete the record
        def delete_company_basic_info(self, keyword, condition):
            with Session() as session:
                basic = Session.query(company_basic_info).filter_by(compamy_basic_info.keyword == condition).first()
                Session.delete(Basic)
                Session.commit()

        def delete_company_financial_info(self, keyword, condition):
            with Session() as session:
                financial = Session.query(company_financial_info).filter_by(company_fiancial_info.keyword == condition).first()
                Session.delete(Financial)
                Session.commit()

        def delete_company_shaerholder_info(self, keyword, condition):
            with Session() as session:
                shareholder = Session.query(company_shareholder_info).filter_by(company_shareholder_info.keyword == condition).first()
                Session.delete(Shareholder)
                Session.commit()

        def delete_daily_news_url(self, keyword, condition):
            with Session() as session:
                dailynews = Session.query(daily_news_url).filter_by(daily_news_url.keyword == condition).first()
                Session.delete(dailynews)
                Session.commit()

        def delete_kline_graph_info(self, keyword, condition):
            with Session() as session:
                kline = Session.query(kline_graph).filter_by(kline_graph.keyword == condition).first()
                Session.delete(Kline)
                Session.commit()

        def delete_transaction_data_seperate(self, keyword, condition):
            with Session() as session:
                transaction = Session.query(transaction_data_seperate).filter_by(transaction_data_seperate.keyword == condition).first()
                Session.delete(Transaction)
                Session.commit()

    def info_query(self):
        #basic query
        def company_basic_info_query(self, keyword, condition):
            with Session() as session:
                basic = Session.query(company_basic_info).filter(company_basic_info.keyword == condition).all()
                data = [dict(zip(basic.keys(),basic)) for result in basic]

        def company_financial_info_query(self, keyword, condition):
            with Session() as session:
                financial = Session.query(company_financial_info).filter(company_financial_info.keyword == condition).all()
                data = [dict(zip(financial.keys(),financial)) for result in financial]


        def company_shareholder_info_query(self, keyword, condition):
            with Session() as session:
                shareholder = Session.query(company_shareholder_info).filter(company_shareholder_info.keyword == condition).all()
                data = [dict(zip(shareholder.keys(),shareholder)) for result in shareholder]

        def daily_news_url_query(self, keyword, condition):
            with Session() as session:
                dailynews = Session.query(daily_news_url).filter(daily_news_url.keyword == condition).all()
                data = [dict(zip(dailynews.keys(),dailynews)) for result in dailynews]

        def kline_graph_query(self, keyword, condition):
            with Session() as session:
                kline = Session.query(kline_graph).filter(kline_graph.keyword == condition).all()
                data = [dict(zip(kline.keys(),kline)) for result in kline]

        def transaction_data_seperate_query(self, fkeyword, condition):
            with Session() as session:
                transaction = Session.query(transaction_data_seperate).filter(transaction_data_seperate.keyword == condition).all()
                data = [dict(zip(transaction.keys(),transaction)) for result in transaction]



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


    def insert_data_to_kline_graph(self, csv_file_path):
        dtype = {
            'open_price': np.float64, 'stock_code': np.string_,
            'close_price': np.float64, 'highest_price': np.float64,
            'lowest_price': np.float64, 'total_amount': np.float64,
            'total_sales': np.float64, 'increase': np.float64,
        }
        data = pd.read_csv('../sh_kline.csv', dtype=dtype, engine='python')
        data.to_sql('kline_graph', engine, if_exists='append', index=False)


    # #create the record
    # def create_company_basic_info(self):
    #     Basic = company_basic_info(
    #
    #     )
    #     Session.add(Basic)
    #     Session.commit()
    #
    #
    # def create_company_financial_info(self):
    #     Financial = company_financial_info(
    #
    #     )
    #     Session.add(Financial)
    #     Session.commit()
    #
    # def create_company_shareholder_info(self):
    #     Shareholder = company_shareholder_info(
    #
    #     )
    #     Session.add(Shareholder)
    #     Session.commit()
    #
    # def create_kline_graph(self):
    #    Kline = kline_graph(
    #
    #    )
    #    Session.add(Kline)
    #    Session.commit()
    #
    # def create_transaction_data_seperate(self):
    #     Transaction = transaction_data_seperate(
    #
    #     )
    #     Session.add(Transaction)
    #     Session.commit()
    #
    # #modify the record
    def modify_company_basic_info(self, keyword, condition, Target):
        with Session() as session:
            basic = Session.query(company_basic_info).filter_by(keyword == condition).first()
            basic.attribute = Target
            Session.commit()

    def modify_company_financial_info(self, keyword, contidion, Target):
        with Session() as session:
            financial = Session.query(company_financial_info).filter_by(keyword == contidion).first()
            financial.attribute = Target
            Session.commit()

    def modify_company_shaerholder_infof(self, keyword, condition, Target):
        with Session() as session:
            shareholder = Session.query(company_shareholder_info).filter_by(keyword == condition).first()
            shareholder.attribute = Target
            Session.commit()

    def modify_kline_graph_info(self, keyword, condition, Target):
        with Session() as session:
            kline = Session.query(kline_graph).filter_by(keyword == condition).first()
            kline.attribute = Target
            Session.commit()

    def modify_transaction_data_seperate(self, keyword, condition, Target):
        with Session() as session:
            transaction = Session.query(transaction_data_seperate).filter_by(keyword == condition).first()
            transaction.attribute = Target
            Session.commit()

    #delete the record
    def delete_company_basic_info(self, keyword, condition):
        with Session() as session:
            basic = Session.query(company_basic_info).filter_by(keyword == condition).first()
            Session.delete(Basic)
            Session.commit()

    def delete_company_financial_info(self, keyword, condition):
        with Session() as session:
            financial = Session.query(company_financial_info).filter_by(keyword == condition).first()
            Session.delete(Financial)
            Session.commit()

    def delete_company_shaerholder_info(self, keyword, condition):
        with Session() as session:
            shareholder = Session.query(company_shareholder_info).filter_by(keyword == condition).first()
            Session.delete(Shareholder)
            Session.commit()


    def delete_kline_graph_info(self, keyword, condition):
        with Session() as session:
            kline = Session.query(kline_graph).filter_by(keyword == condition).first()
            Session.delete(Kline)
            Session.commit()

    def delete_transaction_data_seperate(self, keyword, condition):
        with Session() as session:
            transaction = Session.query(transaction_data_seperate).filter_by(keyword == condition).first()
            Session.delete(Transaction)
            Session.commit()

    #basic query
    def company_basic_info_query(self, keyword, condition):
        with Session() as session:
            basic = Session.query(company_basic_info).filter(keyword == condition).all()
            data = [dict(zip(basic.keys(),basic)) for result in basic]

    def company_financial_info_query(self, keyword, condition):
        with Session() as session:
            financial = Session.query(company_financial_info).filter(keyword == condition).all()
            data = [dict(zip(financial.keys(),financial)) for result in financial]


    def company_shareholder_info_query(self, keyword, condition):
        with Session() as session:
            shareholder = Session.query(company_shareholder_info).filter(keyword == condition).all()
            data = [dict(zip(shareholder.keys(),shareholder)) for result in shareholder]


    def kline_graph_query(self, keyword, condition):
        with Session() as session:
            kline = Session.query(kline_graph).filter(keyword == condition).all()
            data = [dict(zip(kline.keys(),kline)) for result in kline]


    def transaction_data_seperate_query(self, fkeyword, condition):
        with Session() as session:
            transaction = Session.query(transaction_data_seperate).filter(keyword == condition).all()
            data = [dict(zip(transaction.keys(),transaction)) for result in transaction]



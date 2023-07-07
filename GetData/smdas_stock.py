import datetime
import requests
from lxml import etree
import pymysql
import pandas as pd
import os

from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import column_property, relationship, deferred
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import dotenv_values

config = dotenv_values(".env")

host=config["host"]
port=config["port"]
user=config["user"]
passwd=config["passwd"]
db=config["db2"]
connect_timeout=config["connect_timeout"]

db_url = "mariadb+mariadbconnector://user:passwd@host:port/db?charset=utf8"
engine = create_engine(db_url)

Base = declarative_base()

#class the table
class company_basic_info(Base):
    __tablename__ = 'company_basic_info'
    id = Column(int,primary_key=True)
    stock_code = Column(str)
    name = Column(str)
    intro = Column(str)
    leader = Column(str)
    distribution = Column(str)
    notice = Column(str)

class company_financial_info(Base):
    __tablename__ = 'company_financial_info'
    id = Column(int,primary_key=True)
    stock_code = Column(str)
    property = Column(float)
    liability = Column(float)
    interest = Column(float)
    income = Column(float)
    profit = Column(float)
    asset_turnover = Column(float)
    account_receivable_turnover = Column(float)
    inventory_turnover = Column(float)
    operating_cycle = Column(float)

class company_shareholder_info(Base):
    __tablename__ = 'company_shareholder_info'
    id = Column(int,primary_key=True)
    stock_code = Column(str)
    name = Column(str)
    identity = Column(str)
    counting = Column(int)
    rate = Column(float)
    period = Column(datetime.date)

class kline_graph(Base):
    __tablename__ = 'kline_graph'
    id = Column(int, primary_key=True)
    stock_code = Column(str)
    date = Column(datetime.date)
    total_amount = Column(int)
    total_sales = Column(float)
    average_price = Column(float)
    open_price = Column(float)
    close_price = Column(float)
    highest_price = Column(float)
    lowest_price = Column(float)
    increase = Column(float)

class transaction_data_seperate(Base):
    __tablename__ = 'transaction_data_seperate'
    id = Column(int, primary_key=True)
    stock_code = Column(str)
    date = Column(datetime.date)
    amount = Column(int)
    price = Column(float)

Session = sessionmaker(bind = engine)
Session = Session()

#create the record
def create_company_basic_info(self):
    Basic = company_basic_info(

    )
    Session.add(Basic)
    Session.commit()


def create_company_financial_info(self):
    Financial = company_financial_info(

    )
    Session.add(Financial)
    Session.commit()

def create_company_shareholder_info(self):
    Shareholder = company_shareholder_info(

    )
    Session.add(Shareholder)
    Session.commit()

def create_kline_graph(self):
    Kline = kline_graph(

    )
    Session.add(Kline)
    Session.commit()

def create_transaction_data_seperate(self):
    Transaction = transaction_data_seperate(

    )
    Session.add(Transaction)
    Session.commit()

#modify the record
def modify_company_basic_info(self):
    Basic = Session.query(company_basic_info).filter_by(Query Criteria).first()
    Basic.attribute = 'Target'
    Session.commit()

def modify_company_financial_info(self):
    Financial = Session.query(company_financial_info).filter_by(Query Criteria).first()
    Financial.attribute = 'Target'
    Session.commit()

def modify_company_shaerholder_info(self):
    Shareholder = Session.query(company_shareholder_info).filter_by(Query Criteria).first()
    Shareholder.attribute = 'Target'
    Session.commit()

def modify_kline_graph_info(self):
    Kline = Session.query(kline_graph).filter_by(Query Criteria).first()
    Kline.attribute = 'Target'
    Session.commit()

def modify_transaction_data_seperate(self):
    Transaction = Session.query(transaction_data_seperate).filter_by(Query Criteria).first()
    Transaction.attribute = 'Target'
    Session.commit()

#delete the record
def delete_company_basic_info(self):
    Basic = Session.query(company_basic_info).filter_by(Query Criteria).first()
    Session.delete(Basic)
    Session.commit()

def delete_company_financial_info(self):
    Financial = Session.query(company_financial_info).filter_by(Query Criteria).first()
    Session.delete(Financial)
    Session.commit()

def delete_company_shaerholder_info(self):
    Shareholder = Session.query(company_shareholder_info).filter_by(Query Criteria).first()
    Session.delete(Shareholder)
    Session.commit()

def delete_kline_graph_info(self):
    Kline = Session.query(kline_graph).filter_by(Query Criteria).first()
    Session.delete(Kline)
    Session.commit()

def delete_transaction_data_seperate(self):
    Transaction = Session.query(transaction_data_seperate).filter_by(Query Criteria).first()
    Session.delete(Transaction)
    Session.commit()

#basic query
def company_basic_info_query(self):
    Basic = Session.query(company_basic_info).filter(keyword condition).all()

def company_financial_info_query(self):
    Financial = Session.query(company_financial_info).filter(keyword condition).all()

def company_shareholder_info_query(self):
    Shareholder = Session.query(company_shareholder_info).filter(keyword condition).all()

def kline_graph_query(self):
    Kline = Session.query(kline_graph).filter(keyword condition).all()

def transaction_data_seperate_query(self):
    Transaction = Session.query(transaction_data_seperate).filter(keyword condition).all()
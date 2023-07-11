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

class SmdasDiscretionaryStock:

    def __init__(self):
        config = dotenv_values(".env")
        host = config["host"]
        port = config["port"]
        user = config["user"]
        passwd = config["passwd"]
        db = config["db3"]
        connect_timeout = config["connect_timeout"]

        db_url = "".join(["mysql+pymysql://", user, ":", passwd, "@", host, ":", port, "/", db, "?charset=utf8"])
        self.engine = create_engine(db_url)
        self.Base = declarative_base()

        Session = sessionmaker(engine)
        self.session = Session()


    def table_create(self):
    # class the table
        class discretionary_stock(self.Base):
            __tablename__ = 'discretionary_stock'
            id = Column(int, primary_key=True)
            account = Column(str)
            stock_code = Column(str)


        class personality_module(self.Base):
            __tablename__ = 'discretionary_stock'
            id = Column(int, primary_key=True)
            account = Column(str)
            preference = Column(str)
            prediction = Column(str)
            history = Column(str)


    def record_create(self):
    # create the record
        def create_discretionary_stock(self, account1, stockcode1):
            with Session() as session:
                discretionary = discretionary_stock(
                    account = account1, stockcode = stockcode1
                )
                Session.add(discretionary_stock)
                Session.commit()


        def create_personality_module(self, account2, preference2, prediction2, history2):
            with Session() as session:
                personality = personality_module(
                    account = account2, preference = preference2,
                    prediction = prediction2, history = history2
                )
                Session.add(personality_module)
                Session.commit()


    # modify the record
    def record_modify(self):
        def modify_discretionary_stock(self, keyword, condition, Target):
            with Session() as session:
                discretionary = Session.query(discretionary_stock).filter_by(keyword == condition).first()
                discretionary.attribute = Target
                Session.commit()


        def modify_personality_module(self, keyword, condition, Target):
            with Session() as session:
                personality = Session.query(personality_module).filter_by(keyword == condition).first()
                personality.attribute = Target
                Session.commit()


    # delete the record
    def record_delete(self):
        def delete_discretionary_stock(self, keyword, condition):
            with Session() as session:
                discretionary = Session.query(discretionary_stock).filter_by(discretionary_stock.keyword == condition).first()
                Session.delete(discretionary)
                Session.commit()


        def delete_personality_module(self, keyword, condition):
            with Session() as session:
                personality = Session.query(personality_module).filter_by(personality_module.keyword == condition).first()
                Session.delete(personality)
                Session.commit()


    # basic query
    def info_query(self):
        def discretionary_stock_query(self, keyword, condition):
            with Session() as session:
                discretionary = Session.query(discretionary_stock).filter(discretionary_stock.keyword == condition).all()
                data = [dict(zip(discretionary.keys(),discretionary)) for results in discretionary]


        def personality_module_query(self, keyword, condition):
            with Session() as session:
                personality = Session.query(personality_module).filter(personality_module.keyword == condition).all()
                data = [dict(zip(personality.keys(),personality)) for result in personality]

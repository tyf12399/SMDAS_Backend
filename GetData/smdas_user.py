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

class SmdasUser:
    def __init__(self):
        config = dotenv_values(".env")

        host=config["host"]
        port=config["port"]
        user=config["user"]
        passwd=config["passwd"]
        db=config["db1"]
        connect_timeout=config["connect_timeout"]

        db_url = "".join(["mariadb+mariadbconnector://", user, ":", passwd, "@", host, ":", port, "/", db, "?charset=utf8"])
        self.engine = create_engine(db_url)
        self.Base = declarative_base()

        Session = sessionmaker(bind = self.engine)
        self.session = Session()

    def table_create(self):
        #class the table
        class info(self.Base):
            __tablename__ = 'info'
            id = Column(int,primary_key=True)
            account = Column(str)
            password = Column(str)
            identity = Column(bool)
            question = Column(str)
            answer = Column(str)
            nickname = Column(str)

    def record_create(self):
        #create the record
        def create_user(self, account1, password1, identity1, question1, answer1, nickname1):
            information = info(
                account = account1, password = password1, identity = identity1,
                question = question1, answer = answer1, nickname = nickname1
            )
            Session.add(information)
            Session.commit()

    def record_modify(self):
        #modify the record
        def modify_user(self, keyword, condition, Target):
            information = Session.query(info).filter_by(info.keyword == condition).first()
            information.attribute = Target
            Session.commit()

    def record_delete(self):
        #delete the record
        def delete_user(self, keyword, condition):
            information = Session.query(info).filter_by(info.keyword == condition).first()
            Session.delete(information)
            Session.commit()

    def info_query(self):
        #basic query
        def info_query(self, keyword, condition):
            information = Session.query(info).filter(info.keyword == condition).all()
            data = [dict(zip(information.keys(), information)) for result in information]



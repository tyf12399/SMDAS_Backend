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

config = dotenv_values(".env")

host=config["host"]
port=config["port"]
user=config["user"]
passwd=config["passwd"]
db=config["db1"]
connect_timeout=config["connect_timeout"]

db_url = "".join(["mariadb+mariadbconnector://", user, ":", passwd, "@", host, ":", port, "/", db, "?charset=utf8"])
engine = create_engine(db_url)

Base = declarative_base()

#class the table
class info(Base):
    __tablename__ = 'info'
    id = Column(int,primary_key=True)
    account = Column(str)
    password = Column(str)
    identity = Column(bool)
    question = Column(str)
    answer = Column(str)
    nickname = Column(str)

Session = sessionmaker(bind=engine)
Session = Session()

#create the record
def create_user(self):
    Info = info(

    )
    Session.add(Info)
    Session.commit()

#modify the record
def modify_user(QueryCriteria):
    Info = Session.query(info).filter_by(QueryCriteria).first()
    Info.attribute = 'Target'
    Session.commit()

#delete the record
def delete_user(QueryCriteria):
    Info = Session.query(info).filter_by(QueryCriteria).first()
    Session.delete(Info)
    Session.commit()

#basic query
def info_query(keywordcondition):
    Info = Session.query(info).filter(keywordcondition).all()


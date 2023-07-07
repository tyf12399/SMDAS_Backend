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
db=config["db1"]
connect_timeout=config["connect_timeout"]

db_url = "mariadb+mariadbconnector://user:passwd@host:port/db?charset=utf8"
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
def modify_user(self):
    Info = Session.query(info).filter_by(Query Criteria).first()
    Info.attribute = 'Target'
    Session.commit()

#delete the record
def delete_user(self):
    Info = Session.query(info).filter_by(Query Criteria).first()
    Session.delete(Info)
    Session.commit()

#basic query
def info_query(self):
    Info = Session.query(info).filter(keyword condition).all()


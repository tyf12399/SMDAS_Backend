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
host = config["host"]
port = config["port"]
user = config["user"]
passwd = config["passwd"]
db = config["db3"]
connect_timeout = config["connect_timeout"]

db_url = "".join(["mysql+pymysql://", user, ":", passwd, "@", host, ":", port, "/", db, "?charset=utf8"])
engine = create_engine(db_url)
Base = declarative_base()
Session = sessionmaker(engine)


# class the table
class discretionary_stock(Base):
    __tablename__ = 'discretionary_stock'
    id = Column(int, primary_key=True)
    account = Column(str)
    stock_code = Column(str)


class personality_module(Base):
    __tablename__ = 'discretionary_stock'
    id = Column(int, primary_key=True)
    account = Column(str)
    preference = Column(str)
    prediction = Column(str)
    history = Column(str)


# create the record
def create_discretionary_stock(self):
    with Session() as session:
        discretionary = discretionary_stock(

        )
        Session.add(discretionary_stock)
        Session.commit()


def create_personality_module(self):
    with Session() as session:
        personality = personality_module(

        )
        Session.add(personality_module)
        Session.commit()


# modify the record
def modify_discretionary_stock(QueryCriteria, Target):
    with Session() as session:
        discretionary = Session.query(discretionary_stock).filter_by(QueryCriteria).first()
        discretionary.attribute = 'Target'
        Session.commit()


def modify_personality_module(QueryCriteria, Target):
    with Session() as session:
        personality = Session.query(personality_module).filter_by(QueryCriteria).first()
        personality.attribute = 'Target'
        Session.commit()


# delete the record
def delete_discretionary_stock(QueryCriteria):
    with Session() as session:
        discretionary = Session.query(discretionary_stock).filter_by(QueryCriteria).first()
        Session.delete(discretionary)
        Session.commit()


def delete_personality_module(QueryCriteria):
    with Session() as session:
        personality = Session.query(personality_module).filter_by(QueryCriteria).first()
        Session.delete(personality)
        Session.commit()


# basic query
def discretionary_stock_query(keywordcondition):
    with Session() as session:
        discretionary = Session.query(discretionary_stock).filter(keywordcondition).all()


def personality_module_query(keywordcondition):
    with Session() as session:
        personality = Session.query(personality_module).filter(keywordcondition).all()

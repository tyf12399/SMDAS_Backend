from dotenv import dotenv_values
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

config = dotenv_values(".env")

host = config["host"]
port = config["port"]
user = config["user"]
passwd = config["passwd"]
db = config["db3"]
connect_timeout = config["connect_timeout"]

db_url = "".join(["mariadb+mariadbconnector://", user, ":", passwd, "@", host, ":", port, "/", db, "?charset=utf8"])
engine = create_engine(db_url)

Base = declarative_base()


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


Session = sessionmaker(bind=engine)
Session = Session()


# create the record
def create_discretionary_stock(self):
    Discretionary = discretionary_stock(

    )
    Session.add(discretionary_stock)
    Session.commit()


def create_personality_module(self):
    Personality = personality_module(

    )
    Session.add(personality_module)
    Session.commit()


# modify the record
def modify_discretionary_stock(self):
    Discretionary = Session.query(discretionary_stock).filter_by(Query
    Criteria).first()
    Discretionary.attribute = 'Target'
    Session.commit()


def modify_personality_module(self):
    Personality = Session.query(personality_module).filter_by(Query
    Criteria).first()
    Personality.attribute = 'Target'
    Session.commit()


# delete the record
def delete_discretionary_stock(self):
    Discretionary = Session.query(discretionary_stock).filter_by(Query
    Criteria).first()
    Session.delete(Discretionary)
    Session.commit()


def delete_personality_module(self):
    Personality = Session.query(personality_module).filter_by(Query
    Criteria).first()
    Session.delete(Personality)
    Session.commit()


# basic query
def discretionary_stock_query(self):
    Discretionary = Session.query(discretionary_stock).filter(keyword
    condition).all()


def personality_module_query(self):
    Personality = Session.query(personality_module).filter(keyword
    condition).all()

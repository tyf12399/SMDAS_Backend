from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from get_data.smdas_discretionary_stock import DiscretionaryStock, PersonalityModule

config = dotenv_values("../.env")

host = config["host"]
port = config["port"]
user = config["user"]
passwd = config["passwd"]
db = config["db3"]
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


# create the record
def create_discretionary_stock(account1, stockcode1):
    with Session() as session:
        discretionary = DiscretionaryStock(
            account=account1, stockcode=stockcode1
        )
        Session.add(discretionary)
        Session.commit()


def create_personality_module(account2, preference2, prediction2, history2):
    with Session() as session:
        personality = PersonalityModule(
            account=account2, preference=preference2,
            prediction=prediction2, history=history2
        )
        Session.add(personality)
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
            discretionary = Session.query(discretionary_stock).filter_by \
                (discretionary_stock.keyword == condition).first()
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
            data = [dict(zip(discretionary.keys(), discretionary)) for results in discretionary]

    def personality_module_query(self, keyword, condition):
        with Session() as session:
            personality = Session.query(personality_module).filter(personality_module.keyword == condition).all()
            data = [dict(zip(personality.keys(), personality)) for result in personality]

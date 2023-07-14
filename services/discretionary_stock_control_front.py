from dotenv import dotenv_values
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from get_data.smdas_discretionary_stock import DiscretionaryStock

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


# # create the record
# def create_discretionary_stock(account1, stock_code1):
#     with Session() as session:
#         discretionary = DiscretionaryStock(account=account1, stock_code=stock_code1)
#         session.add(discretionary)
#         session.commit()
#
#
# def create_personality_module(account2, preference2, prediction2, history2):
#     with Session() as session:
#         personality = PersonalityModule(
#             account=account2,
#             preference=preference2,
#             prediction=prediction2,
#             history=history2,
#         )
#         session.add(personality)
#         session.commit()
#
# #
# # update the record
# def update_discretionary_stock(keyword, condition, Target):
#     with Session() as session:
#         discretionary = (
#             Session.query(DiscretionaryStock).filter_by(keyword == condition).first()
#         )
#         discretionary.attribute = Target
#         Session.commit()
#
#
# def update_personality_module(keyword, condition, Target):
#     with Session() as session:
#         personality = (
#             Session.query(PersonalityModule).filter_by(keyword == condition).first()
#         )
#         personality.attribute = Target
#         Session.commit()
#
#
# # delete the record
# def delete_discretionary_stock(keyword, condition):
#     with Session() as session:
#         discretionary = (
#             Session.query(DiscretionaryStock)
#             .filter_by(DiscretionaryStock.keyword == condition)
#             .first()
#         )
#         Session.delete(discretionary)
#         Session.commit()
#
#
# def delete_personality_module(keyword, condition):
#     with Session() as session:
#         personality = (
#             Session.query(personality_module)
#             .filter_by(personality_module.keyword == condition)
#             .first()
#         )
#         Session.delete(personality)
#         Session.commit()


# # basic query
# def discretionary_stock_query(account, stock_code):
#     with Session() as session:
#         discretionary = (
#             select(DiscretionaryStock)
#             .where(DiscretionaryStock.account.in_([account]))
#             .where(DiscretionaryStock.stock_code.in_([stock_code]))
#         )
#
#
# def personality_module_query(account):
#     with Session() as session:
#         personality = select(PersonalityModule).where(
#             PersonalityModule.account.in_([account])
#         )

from dotenv import dotenv_values
from sqlalchemy import create_engine, select, insert, delete, and_
from sqlalchemy.orm import Session

from get_data.smdas_discretionary_stock import DiscretionaryStock
from get_data.smdas_stock import KlineGraph

config = dotenv_values(".env")

host = config["host"]
port = config["port"]
user = config["user"]
passwd = config["passwd"]
db1 = config["db3"]
db2 = config["db2"]
connect_timeout = config["connect_timeout"]

db_url1 = "".join(
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
        db1,
        "?charset=utf8",
    ]
)

db_url2 = "".join(
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
        db2,
        "?charset=utf8",
    ]
)

engine1 = create_engine(db_url1)
engine2 = create_engine(db_url2)


# create the record
def create_discretionary_stock(account1: str, stock_code1: str):
    with engine1.begin() as session:
        session.execute(
            insert(DiscretionaryStock),
            [{"account": account1, "stock_code": stock_code1}],
        )

    return {"ifaddms": True}


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
# delete the record
def delete_discretionary_stock(account: str, stock_code: str):
    with engine1.begin() as session:
        discretionary = (
            delete(DiscretionaryStock)
            .where(DiscretionaryStock.account == account)
            .where(DiscretionaryStock.stock_code == stock_code)
        )
        session.execute(discretionary)
    return {"ifdelms": True}


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


# basic query
def discretionary_stock_query(account: str):
    with engine1.begin() as session:
        stmt = select(DiscretionaryStock)

        conditions = []
        conditions.append(DiscretionaryStock.account == account)

        if conditions:
            stmt = stmt.where(and_(*conditions))

        result = session.execute(stmt).all()
        result = [int(item[2]) for item in result]

    with engine2.begin() as session:
        stmt = (
            select(KlineGraph)
            .where(KlineGraph.stock_code.in_(result))
            .where(KlineGraph.date.in_(["2023-07-07"]))
        )
        finalresult = session.execute(stmt).all()

        result = [
            {
                "mysid": str(item[1]),
                "mysdate": str(item[2]),
                "mysprice": str(item[4] / item[3]),
                "myincrease": str(item[9]),
            }
            for item in finalresult
        ]
        return result


#
#
# def personality_module_query(account):
#     with Session() as session:
#         personality = select(PersonalityModule).where(
#             PersonalityModule.account.in_([account])
#         )
# 自选股添加（）；自选股删除（）；insert, delete, query

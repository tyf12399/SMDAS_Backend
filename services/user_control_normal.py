from datetime import datetime

from dotenv import dotenv_values
from sqlalchemy import create_engine, update, delete, select, and_
from sqlalchemy.orm import Session

from get_data.smdas_user import Info

config = dotenv_values(".env")

host = config["host"]
port = config["port"]
user = config["user"]
passwd = config["passwd"]
db = config["db1"]
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


def create_user(
    password: str,
    question: str,
    answer: str,
    nickname: str
):
    pass

def update_user_info(
    account: str,
    password: str,
    identity: int,
    question: str,
    answer: str,
    nickname: str,
):
    with engine.begin() as session:
        prep = (
            update(Info)
            .where(Info.account == account)
            .values(password=password)
            .values(identity=identity)
            .values(question=question)
            .values(answer=answer)
            .values(nickname=nickname)
        )
        session.execute(prep)


def check_user(
    account: str,
    password: str,
):
    with engine.begin() as session:
        stmt = select(Info).where(Info.account == account)
        result = session.execute(stmt).all()
        if result[0][2] == password:
            return {"data": [{"ifsuclog": True, "username": result[0][6]}]}
        else:
            return {"data": [{"ifsuclog": False, "username": result[0][6]}]}

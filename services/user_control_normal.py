from dotenv import dotenv_values
from sqlalchemy import create_engine, select, update, delete
from sqlalchemy.orm import Session

from get_data.smdas_user import Info

config = dotenv_values("../.env")

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


def update_user_info(account, password, identity, question, answer, nickname):
    with Session(engine) as session:
        prep = (
            update(Info).where(Info.account.in_(account))
            .values(password=password)
            .values(identity=identity)
            .values(question=question)
            .values(answer=answer)
            .values(nickname=nickname)
        )
        session.execute(prep)


def delete_user(account):
    with Session(engine) as session:
        prep = delete(Info.account.in_(account))
        session.execute(prep)

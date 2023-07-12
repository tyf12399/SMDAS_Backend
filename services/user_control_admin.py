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


def create_user(account, password, identity, question, answer, nickname, state, login_time, create_time):
    with Session(engine) as session:
        info = Info(
            account1=account,
            password1=password,
            identity1=identity,
            question1=question,
            answer1=answer,
            nickname1=nickname,
            state1=state,
            login_time1=login_time,
            create_time1=create_time,
        )

        session.add(info)
        session.commit()


def select_user(account, nickname, state, create_time_start, create_time_end, log_in_time_start, log_in_time_end):
    with Session(engine) as session:
        session.query(Info).filter_by(account=account, nickname=nickname, state=state,
                                      create_time_start=create_time_start, create_time_end=create_time_end,
                                      log_in_time_start=log_in_time_start, log_in_time_end=log_in_time_end)


def delete_user(account1):
    with Session(engine) as session:
        prep = delete(Info).where(Info.account.in_(account1))
        session.execute(prep)


def update_user_question(account2):
    with Session(engine) as session:
        prep = (
            update(Info).where(Info.account.in_(account2))
            .values(question="")
        )
        session.execute(prep)


def update_user_answer(account3):
    with Session(engine) as session:
        prep = (
            update(Info).where(Info.account.in_(account3))
            .values(answer="")
        )
        session.execute(prep)


def update_user_password(account4):
    with Session(engine) as session:
        prep = (
            update(Info).where(Info.account.in_(account4))
            .values(password='123456')
        )
        session.execute(prep)


def update_user_info(account5, nickname5, state5):
    with Session(engine) as session:
        prep = (
            update(Info).where(Info.account.in_(account5))
            .values(nickname=nickname5, state=state5)
        )
        session.execute(prep)

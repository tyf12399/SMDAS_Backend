from dotenv import dotenv_values
from sqlalchemy import create_engine, select
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
        query = select(Info).where(Info.nickname.in_([nickname]))\
            .where(Info.account.in_([account]))\
            .where(Info.state.in_([state]))\
            .where(Info.create_time.in_([account]))\
            .where(Info.create_time.in_([account]))\
            .where(Info.login_time.in_([account]))\
            .where(Info.login_time.in_([account]))
        for user in session.scalars(query):
            print(f"{user}")
        return query


def delete_user():
    with Session(engine) as session:



if __name__ == '__main__':
    select_user()

from datetime import datetime

from dotenv import dotenv_values
from sqlalchemy import Result, create_engine, update, delete, select, and_, between
from sqlalchemy.orm import Session, aliased

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


def select_user(
    account: str = None,
    nickname: str = None,
    state: str = None,
    create_time_start: str = None,
    create_time_end: str = None,
    log_in_time_start: str = None,
    log_in_time_end: str = None,
):
    with Session(engine) as session:
        stmt = select(Info)

        # 构建查询条件
        conditions = []
        if account is not None:
            conditions.append(Info.account == account)
        if nickname is not None:
            conditions.append(Info.nickname == nickname)
        if state is not None:
            conditions.append(Info.state == state)
        if log_in_time_start is not None:
            conditions.append(
                Info.login_time.between(log_in_time_start, log_in_time_end)
            )
        if create_time_start is not None:
            conditions.append(
                Info.login_time.between(create_time_start, create_time_end)
            )

        # 应用查询条件
        if conditions:
            stmt = stmt.where(and_(*conditions))

        # 执行查询
        result = session.execute(stmt).all()
        result = [
            {
                "account": item[0].account,
                "nickname": item[0].nickname,
                "state": item[0].state,
                "login_at": datetime.strftime(item[0].login_time, "%Y-%m-%d"),
                "created_at": datetime.strftime(item[0].create_time, "%Y-%m-%d"),
            }
            for item in result
        ]
        return result


def delete_user(account: str):
    with engine.begin() as session:
        prep = delete(Info).where(Info.account == account)
        session.execute(prep)


def update_user_question(account: str):
    with engine.begin() as session:
        prep = (
            update(Info).where(Info.account == account).values(question="", answer="")
        )
        session.execute(prep)


def update_user_password(account: str):
    with engine.begin() as session:
        prep = update(Info).where(Info.account == account).values(password="123456")
        session.execute(prep)


def update_user_info(account: str, nickname: str, state: int) -> None:
    """
    To update the user_info in the front end.
    :param account: User's account.
    :param nickname: User's nickname.
    :param state: To imply the state of the user.
    :return:
    """
    with engine.begin() as session:
        prep = (
            update(Info)
            .where(Info.account == account)
            .values(nickname=nickname, state=state)
        )
        session.execute(prep)

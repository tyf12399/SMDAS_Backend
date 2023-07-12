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
            print(stmt)

        # 执行查询
        result = session.execute(stmt).all()

        result = [item[0].mapping() for item in result]
        return result


def delete_user(account):
    with Session(engine) as session:
        prep = delete(Info).where(Info.account.in_(account))
        session.execute(prep)


def update_user_question(account):
    with Session(engine) as session:
        prep = update(Info).where(Info.account.in_(account)).values(question="")
        session.execute(prep)


def update_user_answer(account):
    with Session(engine) as session:
        prep = update(Info).where(Info.account.in_(account)).values(answer="")
        session.execute(prep)


def update_user_password(account):
    with Session(engine) as session:
        prep = update(Info).where(Info.account.in_(account)).values(password="123456")
        session.execute(prep)


def update_user_info(account, nickname, state):
    with Session(engine) as session:
        prep = (
            update(Info)
            .where(Info.account.in_(account))
            .values(nickname=nickname, state=state)
        )
        session.execute(prep)

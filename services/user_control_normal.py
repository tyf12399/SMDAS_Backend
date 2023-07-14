from datetime import datetime
import hashlib

from dotenv import dotenv_values
from sqlalchemy import create_engine, update, delete, select, and_, insert
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


def create_user(password: str, question: str, answer: str, nickname: str):
    account = hashlib.md5((password+datetime.now().strftime("%Y%m%d%H%M%S")).encode("utf-8")).digest()[:16].hex()
    with engine.begin() as session:
        session.execute(
            insert(Info),
            [
                {
                    "account": account,
                    "password": password,
                    "question": question,
                    "answer": answer,
                    "nickname": nickname,
                    "identity": 1,
                    "login_time": datetime.now(),
                    "create_time": datetime.now(),
                }
            ],
        )

    return {"ifreg": True, "ifqa": True, "account": account}


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
            return {"ifsuclog": True, "username": result[0][6]}
        else:
            return {"ifsuclog": False, "username": result[0][6]}


def reset_password_get_question(account: str):
    """
    Get user's security question
    :param account: user's account
    :return: security question
    """
    with engine.begin() as session:
        stmt = select(Info)
        conditions = []
        conditions.append(Info.account == account)
        if conditions:
            stmt = stmt.where(and_(*conditions))

        result = session.execute(stmt).all()
        result_question = [(item[4]) for item in result]
        print(result_question)
        result_answer = [(item[5]) for item in result]
        print(result_answer)
        return result_question




import os

from dotenv import dotenv_values
from sqlalchemy import Column, SMALLINT, BIGINT, TEXT, DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

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
Base = declarative_base()

Session = sessionmaker(bind=engine)


class Info(Base):
    __tablename__ = "info"
    id = Column("id", BIGINT, primary_key=True)
    account = Column("account", TEXT)
    password = Column("password", TEXT)
    identity = Column("identity", SMALLINT)
    question = Column("question", TEXT)
    answer = Column("answer", TEXT)
    nickname = Column("nickname", TEXT)
    state = Column("state", SMALLINT)
    login_time = Column("login_time", DATETIME)
    create_time = Column("create_time", DATETIME)

    def __init__(
        self,
        id=None,
        account=None,
        password=None,
        identity=None,
        question=None,
        answer=None,
        nickname=None,
        state=None,
        login_time=None,
        create_time=None,
    ):
        self.id = id
        self.account = account
        self.password = password
        self.identity = identity
        self.question = question
        self.answer = answer
        self.nickname = nickname
        self.state = state
        self.login_time = login_time
        self.create_time = create_time

    def __repr__(self):
        return (
            "<Info(id='%s', account='%s', password='%s', identity='%s', question='%s', answer='%s', nickname='%s', state='%s', login_time='%s', create_time='%s')>"
            % (
                self.id,
                self.account,
                self.password,
                self.identity,
                self.question,
                self.answer,
                self.nickname,
                self.state,
                self.login_time,
                self.create_time,
            )
        )

    def add(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()


if __name__ == "__main__":
    info = Info(
        account="1",
        password="2",
        identity=1,
        question="1",
        answer="2",
        nickname="1",
        state=1,
        login_time="2021-07-01",
        create_time="2021-07-01",
    )
    info.add()

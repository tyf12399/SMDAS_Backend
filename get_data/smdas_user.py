from datetime import datetime

from sqlalchemy import Column, TEXT, DATETIME, SMALLINT, BIGINT
from sqlalchemy.orm import DeclarativeBase


# class the table
class Base(DeclarativeBase):
    pass


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

    def mapping(self):
        """convert to dict"""
        return {
            "id": self.id,
            "account": self.account,
            "password": self.password,
            "identity": self.identity,
            "question": self.question,
            "answer": self.answer,
            "nickname": self.nickname,
            "state": self.state,
            "login_at": self.login_time.strftime("%Y-%m-%d"),
            "created_at": self.create_time.strftime("%Y-%m-%d"),
        }

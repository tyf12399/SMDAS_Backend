from sqlalchemy import TEXT, DATETIME, SMALLINT, BIGINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# class the table
class Base(DeclarativeBase):
    pass


class Info(Base):
    __tablename__ = 'info'
    id: Mapped[int] = mapped_column('id', BIGINT, primary_key=True)
    account: Mapped[str] = mapped_column('account', TEXT)
    password: Mapped[str] = mapped_column('password', TEXT)
    identity: Mapped[int] = mapped_column('identity', SMALLINT)
    question: Mapped[str] = mapped_column('question', TEXT)
    answer: Mapped[str] = mapped_column('answer', TEXT)
    nickname: Mapped[str] = mapped_column('nickname', TEXT)
    state: Mapped[int] = mapped_column('state', SMALLINT)
    login_time: Mapped[str] = mapped_column('login_time', DATETIME)
    create_time: Mapped[str] = mapped_column('create_time', DATETIME)

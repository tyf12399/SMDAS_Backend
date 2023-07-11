"""test database connection"""
from dotenv import dotenv_values

from get_data import smdas_user

if __name__ == "__main__":
    info = smdas_user.Info(
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

"""crawler for the website: https://www.eastmoney.com/ and save it in the database"""
import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from get_data.smdas_stock import DailyNewsUrl

config = dotenv_values("../.env")

host = config["host"]
port = config["port"]
user = config["user"]
passwd = config["passwd"]
db = config["db2"]
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


class Crawler:
    """crawler for the website: https://www.eastmoney.com/ and save the finance news"""

    def __init__(self):
        self.url = "https://www.eastmoney.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }

    def get_news(self):
        """
        get the finance news from the website
        :return:
        """
        response = requests.get(self.url, headers=self.headers)
        response.encoding = response.apparent_encoding
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        news_list = soup.find_all("div", class_="nlist")
        finance_news = []
        for _news in news_list:
            link = _news.a.get("href")
            title = _news.a.text
            # if link start with 'https://finance.eastmoney.com/a/', save it
            if link.startswith("https://finance.eastmoney.com/a/"):
                finance_news.append({"title": title, "link": link})
        return finance_news

    def save_news(self):
        """
        save the finance news to the database
        :return:
        """
        finance_news = self.get_news()
        print(len(finance_news))
        with Session(engine) as session:
            session.execute(
                insert(DailyNewsUrl),
                finance_news,
            )
            session.commit()

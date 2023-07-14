"""test database connection"""

from services.user_control_normal import check_user
from services.stock_control_back import (
    company_shareholder_info_query,
    kline_graph_query,
    daily_news_query,
)

if __name__ == "__main__":
    print(daily_news_query())

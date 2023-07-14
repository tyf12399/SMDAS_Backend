"""test database connection"""

from services.discretionary_stock_control_front import (
    discretionary_stock_query,
    create_discretionary_stock,
    delete_discretionary_stock,
)
from services.user_control_normal import check_user, create_user
from services.stock_control_back import (
    company_shareholder_info_query,
    kline_graph_query,
    daily_news_query,
)

if __name__ == "__main__":
    delete_discretionary_stock("0e1fb74fb04f28f7a5ab57b362d68c1d", "000001")

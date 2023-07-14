"""test database connection"""

from services.discretionary_stock_control_front import (
    discretionary_stock_query,
    create_discretionary_stock,
    delete_discretionary_stock,
)
from services.user_control_normal import check_user, create_user, reset_password
from services.stock_control_back import (
    company_shareholder_info_query,
    kline_graph_query,
    daily_news_query,
)
from datetime import datetime
if __name__ == "__main__":
    reset_password('114514', '2', '1234567', '1234567')
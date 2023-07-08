# _*_ coding: utf-8 _*_
"""CMS Apis.

Content management system apis.
"""

from typing import Union, Dict, Any

from fastapi import APIRouter

router = APIRouter(prefix="/backend", tags=["CMS"])


@router.get("/user_list_get")
async def user_list_get(
    current: int,
    pageSize: int,
    id: Union[int, None] = None,
    name: Union[str, None] = None,
    state: Union[bool, None] = None,
    create_start_time: Union[str, None] = None,  # YYYY-MM-DD
    create_end_time: Union[str, None] = None,  # YYYY-MM-DD
    # login time means the time when the user last login
    login_start_time: Union[str, None] = None,  # YYYY-MM-DD
    login_end_time: Union[str, None] = None,  # YYYY-MM-DD
) -> Dict[str, Any]:
    """
    Get user list.
    :param current: current page
    :param pageSize: entries per page
    :param id: user account
    :param name: user nickname
    :param state: 0: normal, 1: banned
    :param create_start_time: create time start
    :param create_end_time: create time end
    :param login_start_time: last login time start
    :param login_end_time: last login time end
    :return: user list
    """
    # TODO(2023-7-8):read data from info table in user database

    return {
        "data": [
            {
                "id": 10001,
                "name": "唐一凡1号",
                "state": 0,
                "created_at": "2020-07-01",
                "login_at": "2023-04-01",
            },
            {
                "id": 10002,
                "name": "唐一凡2号",
                "state": 1,
                "created_at": "2021-08-01",
                "login_at": "2022-11-01",
            },
            {
                "id": 10003,
                "name": "唐一凡3号",
                "state": 0,
                "created_at": "2001-01-01",
                "login_at": "2003-01-01",
            },
            {
                "id": 10004,
                "name": "唐一凡4号",
                "state": 1,
                "created_at": "2021-07-01",
                "login_at": "2023-07-01",
            },
            {
                "id": 10005,
                "name": "唐一凡5号",
                "state": 0,
                "created_at": "2020-08-01",
                "login_at": "2023-07-07",
            },
            {
                "id": 10006,
                "name": "唐一凡6号",
                "state": 1,
                "created_at": "2021-07-01",
                "login_at": "2023-07-01",
            },
        ],
        "page": 1,
        "success": True,
        "total": 6,
    }


@router.post("/user_list_security_question_reset")
async def user_list_security_question_reset(
    id: int,
) -> Dict[str, Any]:
    """
    Reset user security question.
    :param id: user account
    :return: success or fail
    """
    # TODO(2023-7-8):read data and update data from info table in user database

    return {"massage": "success"}


@router.post("/user_list_password_reset")
async def user_list_password_reset(
    id: str,
) -> Dict[str, Any]:
    """
    Reset user password as 123456.
    :param id: user account
    :return: success or fail
    """
    # TODO(2023-7-8):read data and update data from info table in user database

    return {"massage": "success"}


@router.get("/stock_basic_list_get")
async def stock_basic_list_get(
    current: int,
    pageSize: int,
    code: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Dict[str, Any]:
    """
    Get stock basic info list.
    :param current: current page
    :param pageSize: entries per page
    :param code: stock code
    :param name: stock name
    :return: stock basic info list
    """
    # TODO(2023-7-8):read data and update data from company_basic_info table in stock database

    pass


@router.get("/stock_financial_list_get")
async def stock_financial_list_get(
    current: int,
    pageSize: int,
    code: Union[str, None] = None,
) -> Dict[str, Any]:
    """
    Get stock financial info list.
    :param current: current page
    :param pageSize: entries per page
    :param code: stock code
    :return: stock financial info list
    """
    # TODO(2023-7-8):read data and update data from company_financial_info table in stock database

    pass


@router.get("/stock_shareholder_list_get")
async def stock_shareholder_list_get(
    current: int,
    pageSize: int,
    code: Union[str, None] = None,
) -> Dict[str, Any]:
    """
    Get stock shareholder info list.
    :param current: current page
    :param pageSize: entries per page
    :param code: stock code
    :return: stock shareholder info list
    """
    # TODO(2023-7-8):read data and update data from company_shareholder_info table in stock database

    pass


@router.get("/stock_kline_list_get")
async def stock_kline_list_get(
    current: int,
    pageSize: int,
    code: Union[str, None] = None,
    start_time: Union[str, None] = None,  # YYYY-MM-DD
    end_time: Union[str, None] = None,  # YYYY-MM-DD
) -> Dict[str, Any]:
    """
    Get stock kline info list.
    :param current: current page
    :param pageSize: entries per page
    :param code: stock code
    :param start_time: kline info start time
    :param end_time: kline info end time
    :return:
    """
    # TODO(2023-7-8):read data and update data from company_kline_info table in stock database

    pass


@router.get("/stock_transaction_list_get")
async def stock_transaction_list_get(
    current: int,
    pageSize: int,
    code: Union[str, None] = None,
    start_time: Union[str, None] = None,  # YYYY-MM-DD
    end_time: Union[str, None] = None,  # YYYY-MM-DD
) -> Dict[str, Any]:
    """
    Get stock transaction info list.
    :param current: current page
    :param pageSize: entries per page
    :param code: stock code
    :param start_time: transaction info start time
    :param end_time: transaction info end time
    :return:
    """
    # TODO(2023-7-8):read data and update data from company_transaction_info table in stock database

    pass


@router.get("/model_change")
async def model_change():
    """
    Change predictive analytics model.
    :return:
    """
    # TODO(2023-7-8): change predictive analytics model

    pass

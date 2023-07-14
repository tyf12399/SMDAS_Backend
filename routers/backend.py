# _*_ coding: utf-8 _*_
"""CMS Apis.

Content management system apis.
"""

from typing import Union, Dict, Any
import json

from fastapi import APIRouter, Request

from services.user_control_admin import (
    select_user,
    update_user_info,
    update_user_password,
    update_user_question,
    delete_user,
)

from services import stock_control_back

router = APIRouter(prefix="/backend", tags=["CMS"])


# user management
@router.get("/user/list_get")
async def user_list_get(
    current: int,
    pageSize: int,
    account: Union[int, None] = None,
    nickname: Union[str, None] = None,
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
    :param account: user account
    :param nickname: user nickname
    :param state: 0: normal, 1: banned
    :param create_start_time: create time start
    :param create_end_time: create time end
    :param login_start_time: last login time start
    :param login_end_time: last login time end
    :return: user list
    """
    resp = dict()

    data = select_user(
        account,
        nickname,
        state,
        create_start_time,
        create_end_time,
        login_start_time,
        login_end_time,
    )
    resp["total"] = len(data)
    resp["data"] = data[(current - 1) * pageSize : current * pageSize]
    resp["page"] = current
    resp["success"] = True

    return resp


@router.post("/user/info_change")
async def user_info_change(request: Request) -> Dict[str, Any]:
    """
    Change user info.
    :param request: request body { account , nickname , state}
    :return: {"status": "ok"}
    """
    data: bytes = await request.body()
    data: dict = json.loads(data)
    update_user_info(data["account"], data["nickname"], data["state"])
    return {"status": "ok"}


@router.post("/user/info_delete")
async def user_info_delete(request: Request) -> Dict[str, Any]:
    """
    Delete user info.
    :param request:
    :return:
    """
    data: bytes = await request.body()
    data: dict = json.loads(data)
    delete_user(data["account"])
    return {"status": "ok"}


@router.post("/user/reset/password")
async def user_reset_password(request: Request) -> Dict[str, Any]:
    """
    Reset user password to 123456
    :param request:
    :return:
    """
    data: bytes = await request.body()
    data: dict = json.loads(data)
    print(data["account"])
    update_user_password(data["account"])
    return {"status": "ok"}


@router.post("/user/reset/security_question")
async def user_reset_security_question(request: Request) -> Dict[str, Any]:
    """
    Reset user security question to null
    :param request: user id
    :return:
    """
    data: bytes = await request.body()
    data: dict = json.loads(data)
    update_user_question(data["account"])
    return {"status": "ok"}


@router.get("/stock_shareholder/list_get")
async def stock_shareholder_list_get(
    current: int,
    pageSize: int,
    stock_code: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Dict[str, Any]:
    resp = dict()

    data = stock_control_back.company_shareholder_info_query(stock_code, name)
    resp["total"] = len(data)
    resp["data"] = data[(current - 1) * pageSize : current * pageSize]
    resp["page"] = current
    resp["success"] = True
    return resp


@router.post("/stock_shareholder/info_change")
async def stock_shareholder_info_change(request: Request):
    """

    :param request:
    :return:
    """
    data: bytes = await request.body()
    data: dict = json.loads(data)
    print(data)
    stock_control_back.update_company_shareholder_info(
        data["stock_code"],
        data["name"],
        data["identity"],
        data["counting"],
        data["rate"],
    )
    return {"status": "ok"}


@router.post("/stock_shareholder/info_delete")
async def stock_shareholder_info_delete(request: Request):
    data: bytes = await request.body()
    data: dict = json.loads(data)
    stock_control_back.delete_company_shareholder_info(data["stock_code"], data["name"])
    return {"status": "ok"}


@router.get("/kline_graph/list_get")
async def stock_kline_list_get(
    current: int,
    pageSize: int,
    stock_code: Union[str, None] = None,
    start_time: Union[str, None] = None,
    end_time: Union[str, None] = None,
) -> Dict[str, Any]:
    resp = dict()

    data = stock_control_back.kline_graph_query(
        stock_code,
        start_time,
        end_time,
    )
    resp["total"] = len(data)
    resp["data"] = data[(current - 1) * pageSize : current * pageSize]
    resp["page"] = current
    resp["success"] = True
    return resp


@router.post("/kline_graph/info_change")
async def stock_kline_info_change(request: Request):
    data: bytes = await request.body()
    data: dict = json.loads(data)
    stock_control_back.update_kline_graph_info(
        data["stock_code"],
        data["name"],
        data["identity"],
        data["counting"],
        data["rate"],
        data["period"],
    )
    return {"status": "ok"}


@router.post("/kline_graph/info_delete")
async def stock_kline_info_delete(request: Request):
    data: bytes = await request.body()
    data: dict = json.loads(data)
    stock_control_back.delete_company_shareholder_info(data["stock_code"], data["date"])
    return {"status": "ok"}


@router.get("/daily_news/list_get")
async def get_daily_news(
    current: int,
    pageSize: int,
    start_time: Union[str, None] = None,
    end_time: Union[str, None] = None,
):
    resp = dict()

    data = stock_control_back.daily_news_query(start_time, end_time)

    resp["total"] = len(data)
    resp["data"] = data[(current - 1) * pageSize : current * pageSize]
    resp["page"] = current
    resp["success"] = True

    return resp


@router.post("/model/choose")
async def model_choose(request: Request):
    return {"status": "ok"}

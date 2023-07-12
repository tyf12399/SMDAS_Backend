# _*_ coding: utf-8 _*_
"""CMS Apis.

Content management system apis.
"""

from typing import Union, Dict, Any

from fastapi import APIRouter, Request

from services.user_control_admin import select_user

router = APIRouter(prefix="/backend", tags=["CMS"])


# login and logout
@router.get("/currentUser")
async def currentUser():
    """
    Get current user info.
    :return:
    """
    return {
        "data": {
            "name": "admin",
            "id": "admin",
            "access": "admin",
        }
    }


@router.post("/login/account")
async def login(request: Request):
    """
    Login.
    :param request: request body{ username, password, autoLogin }
    :return: response body{ status, type=account, currentAuthority }
    """
    body = await request.body()
    print(body.decode())
    return {"status": "ok", "type": "account", "currentAuthority": "admin"}


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

    user_list = select_user(
        account,
        nickname,
        state,
        create_start_time,
        create_end_time,
        login_start_time,
        login_end_time,
    )
    keys_to_keep = ["account", "nickname", "state", "created_at", "login_at"]

    data = [{key: user[key] for key in keys_to_keep} for user in user_list]
    resp["total"] = len(data)
    resp["data"] = data[(current - 1) * pageSize : current * pageSize]
    resp["page"] = current
    resp["success"] = True

    return resp


@router.post("/user/info_change")
async def user_info_change(request: Request) -> Dict[str, Any]:
    """
    Change user info.
    :param request:
    :return:
    """
    data = await request.body()
    print(data.decode())
    return {"status": "ok"}


@router.post("/user/info_delete")
async def user_info_delete(request: Request) -> Dict[str, Any]:
    """
    Delete user info.
    :param request:
    :return:
    """
    data = await request.body()
    print(data.decode())
    return {"status": "ok"}


@router.post("/user/reset/password")
async def user_reset_password(request: Request) -> Dict[str, Any]:
    """
    Reset user password to 123456
    :param request:
    :return:
    """
    data = await request.body()
    print(data.decode())
    return {"status": "ok"}


@router.post("/user/reset/security_question")
async def user_reset_security_question(request: Request) -> Dict[str, Any]:
    """
    Reset user security question to null
    :param request: user id
    :return:
    """
    data = await request.body()
    print(data.decode())
    return {"status": "ok"}


# stock basic management
@router.get("/stock_basic/list_get")
async def stock_basic_list_get(
    current: int,
    pageSize: int,
    code: Union[str, None] = None,
    name: Union[str, None] = None,
    industry: Union[str, None] = None,
    area: Union[str, None] = None,
    market: Union[str, None] = None,
    exchange: Union[str, None] = None,
    list_status: Union[str, None] = None,
    list_date_start: Union[str, None] = None,  # YYYY-MM-DD
    list_date_end: Union[str, None] = None,  # YYYY-MM-DD
) -> Dict[str, Any]:
    pass

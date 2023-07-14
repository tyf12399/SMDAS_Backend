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

router = APIRouter(tags=["CMS_login"])


# login and logout
@router.get("/currentUser")
async def currentUser():
    return {
        "data": {
            "name": "admin",
            "id": "admin",
            "access": "admin",
        }
    }


@router.post("/login/account")
async def login(request: Request):
    cookie = request.cookies
    print(cookie)
    return {"status": "ok", "type": "account", "currentAuthority": "admin"}


@router.post("/login/outLogin")
async def outLogin(request: Request):
    return {"data: {}, success: true"}

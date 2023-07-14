# _*_ coding: utf-8 _*_
"""CMS Apis.

Content management system apis.
"""

from typing import Union, Dict, Any
import json


from fastapi import APIRouter, Request, Form

from services.user_control_normal import check_user,create_user
from services.stock_control_front import sh_stock_list,sz_stock_list,his_record, select_kline_graph

router = APIRouter(tags=["Frontend"])


@router.post("/user/login")
async def user_login(request: Request):
    body: bytes = await request.body()
    body: dict = json.loads(body)
    account = body["useraccount"]
    passwd = body["passwd"]
    result = check_user(account, passwd)
    return result


@router.post("/user/register")
async def user_register(request: Request):
    body: bytes = await request.body()
    body = json.loads(body)
    resp = create_user(body["password"],body["question"],body["answer"],body["username"])

    return resp



@router.get("/stockmarket/get_hu_stocks")
async def get_hu_stocks():
    resp = sh_stock_list()
    return resp


@router.get("/stockmarket/get_shen_stocks")
async def get_shen_stocks():
    resp = sz_stock_list()
    return resp

@router.post("/stockmarket/get_his_record")
async def get_history_record(request: Request):
    body: bytes = await request.body()
    body: dict = json.loads(body)
    resp = his_record(body["stockid"])
    return resp


@router.post("/stockmarket/get_k_data")
async def k_line_info(request: Request):
    body: bytes = await request.body()
    body: dict = json.loads(body)
    resp = select_kline_graph(body["stockid"])
    return resp

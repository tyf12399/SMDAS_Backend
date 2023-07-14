# _*_ coding: utf-8 _*_
"""CMS Apis.

Content management system apis.
"""

from typing import Union, Dict, Any
import json


from fastapi import APIRouter, Request, Form

from services.user_control_normal import check_user, create_user
from services.stock_control_front import (
    sh_stock_list,
    sz_stock_list,
    his_record,
    select_kline_graph,
)
from services.discretionary_stock_control_front import (
    create_discretionary_stock,
    delete_discretionary_stock,
    discretionary_stock_query,
)
from model.predict import stock_pred

router = APIRouter(tags=["Frontend"])


@router.post("/user/login")
async def user_login(request: Request):
    body: bytes = await request.body()
    body: dict = json.loads(body)
    account = body["useraccount"]
    passwd = body["password"]
    result = check_user(account, passwd)
    return result


@router.post("/user/register")
async def user_register(request: Request):
    body: bytes = await request.body()
    body = json.loads(body)

    resp = create_user(
        body["password"], body["question"], body["answer"], body["nickname"]
    )

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


@router.post("/stockmarket/get_prediction")
async def get_prediction(request: Request):
    body: bytes = await request.body()
    body: dict = json.loads(body)
    resp = stock_pred(body["stockid"]).tolist()
    return resp


@router.post("/mystock/get_my_stock")
async def get_my_stock(request: Request):
    body: bytes = await request.body()
    body: dict = json.loads(body)
    result = discretionary_stock_query(body["account"])
    return result


@router.post("/mystock/add_my_stock")
async def add_my_stock(request: Request):
    body: bytes = await request.body()
    body: dict = json.loads(body)
    create_discretionary_stock(body["useraccount"], body["mystockid"])

    return {"ifaddms": True}


@router.post("/mystock/del_my_stock")
async def delete_my_stock(request: Request):
    body: bytes = await request.body()
    body: dict = json.loads(body)
    delete_discretionary_stock(body["useraccount"], body["mystockid"])

    return {"ifdelms": True}

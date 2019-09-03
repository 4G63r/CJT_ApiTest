#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-09-02 16:44
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.dirname(curPath)
sys.path.append(rootPath)

from time import sleep
from common.login import Login

login = Login()
front_url = login.url
s = login.session


def token():
    url = '{}/voucher/StockCount/blank?user_req_id=e33e804adx16cf12be303'.format(front_url)
    json_r = s.get(url).json()
    return json_r.get('txnToken')


def create_blank_pdd():
    """
    创建空白盘点单
    :return:
    """
    url = '{}/voucher/StockCount?user_req_id=e33e804adx16cf4d2440b'.format(front_url)
    data = {
        "data": {
            "bizTypeId": 100242,
            "departmentId": 706994634096642,
            "bizEmployeeId": 706994634096643,
            "projectId": None,
            "bizDate": 1567475432567,
            "comments": "",
            "warehouseId": 706994636193798,
            "stockCountMethodEnum": "PHYSICAL_COUNT",
            "whsLockStatusEnum": "UNLOCKED",
            "onHandDate": None,
            "txnToken": token()
        }
    }
    json_r = s.post(url, json=data).json()
    return json_r.get('id')


def get_goods_ids(page_size):
    """
    查询商品id
    :param page_size:
    :return: [707000942198784, 707005774036992]
    """
    url = '{}/data/referProduct/InventoryQtyDm.referWithoutWarehouse?pageSize={}&take={}&skip=0&page=1&filter' \
          '=&aggregate=&loadMore=&productTypes=&custId=&warehouse=706994636193798&criteriaStr=productTypeId+%3C%3E' \
          '+100002+AND+statusEnum+%3D+%27A%27+AND+statusEnum+%3D+%27A%27&fields=&recordDuration=true&user_req_id' \
          '=e33e804adx16cf28f28e0'.format(front_url, page_size, page_size, )
    json_data = s.get(url).json().get('data')
    return (i.get('id') for i in json_data)


def delete_goods(goods_ids):
    """
    从盘点单中删除商品
    :param goods_ids: list [x, x]
    :return:
    """
    l = len(goods_ids)
    url = '{}/stockCount/batchRomveDetail?user_req_id=e33e804adx16cf2bac281'.format(front_url)
    data = goods_ids
    json_r = s.post(url, json=data).json()
    if l == json_r.get('successCount'):
        print('成功从盘点单中删除%s件商品' % l)


def add_goods_to_pdd(product_id):
    """

    :param product_id:
    :return: pdd_id
    """
    url = '{}/stockCount/stockCountDetail?user_req_id=e33e804adx16cf4dafacb'.format(front_url)
    data = {
        "masterVoucherId": 715982124089344,
        "warehouseId": 706994636193798,
        "transQty": 1,
        "transUomId": 706994633965796,
        "trans2Qty": None,
        "baseQty": 1,
        "baseUomId": 706994633965796,
        "auxQty": None,
        "trans2ToTransRate": None,
        "trans2ToBaseRate": None,
        "trans2ToAuxRate": None,
        "transToBaseRate": 1,
        "isTransToBaseFloating": False,
        "transToAuxRate": None,
        "auxToBaseRate": None,
        "manualInputFlag": 4097,
        "onHandBaseQty": 0,
        "retailPrice": None,
        "retailAmount": None,
        "productId": product_id,
        "inventoryLotNo": None,
        "inventoryLotCreationDate": None,
        "inventoryLotExpirationDate": None,
        "barCode": "",
        "itemBarcode": ""
    }
    json_r = s.post(url, json=data).json()
    return json_r


def add_price(pdd_id):
    url = '{}/stockCount/batchUpdate?user_req_id=e33e804adx16cf4df80f6'.format(front_url)
    data = [{
        "id": pdd_id,
        "price": 1,
        "amount": 1,
        "flag": 1
    }]
    s.put(url, json=data)


ids = get_goods_ids(1)
n = 1
for i in ids:
    print(n)
    pdd_id = add_goods_to_pdd(i)
    add_price(pdd_id)
    n += 1
    sleep(0.3)

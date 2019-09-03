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
          '+100002+AND+statusEnum+%3D+%27A%27+AND+statusEnum+%3D+%27A%27&fields=&recordDuration=None&user_req_id' \
          '=e33e804adx16cf28f28e0'.format(front_url, page_size, page_size, )
    json_data = s.get(url).json().get('data')
    return (i.get('id') for i in json_data)


def update_goods_name(product_id, n):
    url = '{}/entity/Product/{}?user_req_id=e33e804adx16cf55763c9'.format(front_url, product_id)
    data = {
        "id": product_id,
        "productTypeId": 100001,
        # "code": "0000007",
        "taxRate": 0,
        "isMultiSpecEnabled": False,
        "statusEnum": "A",
        "createdUserId": 61000385709,
        "createdStamp": 1566806823000,
        "lastUpdatedUserId": 61000385709,
        "lastUpdatedStamp": 1566807360000,
        "parentId": 706994633965779,
        "name": "性能测试UI%s" % n,
        "valuationMethodEnum": "MOVING_AVG",
        "createdUserName": "15899991005",
        "updatedUserName": "15899991005",
        "baseUomId": 706994633965796,
        "salesUomId": 706994633965796,
        "purchaseUomId": 706994633965796,
        "inventoryUomId": 706994633965796,
        "isPurchasable": None,
        "isMadeBySelf": False,
        "isSalable": None,
        "isConsumedByProd": False,
        "isMultiUomEnabled": False,
        "productUomGroup": [],
        "lotCtrlEnabled": False,
        "lotExpCtrlEnabled": False,
        "shelfLifeUomEnum": "DAY",
        "priceBaseComp": [{
            "id": 707007521226757,
            "retailPrice": None,
            "stdWholesalePrice": None,
            "uomId": 706994633965796,
            "refCostPrice": None,
            "maxPurchasePrice": None,
            "stdPurchasePrice": None,
            "level1Price": None,
            "level2Price": None,
            "level3Price": None,
            "level4Price": None,
            "level5Price": None,
            "level6Price": None,
            "level7Price": None,
            "level8Price": None,
            "level9Price": None,
            "level10Price": None,
            "minSalePrice": None,
            "editFlag": "update",
            "sequenceNum": 0
        }],
        "primaryImageList": [],
        "detailImageList": [],
        "productLabelList": [{
            "id": 707776183795739,
            "label": "新品"
        }]
    }
    json_r = s.put(url, json=data).json()
    if json_r.get('id') == product_id:
        print('OK')


def get_goods_by_page_id(page_id):
    url = '{}/data/grid/Product.list?user_req_id=e33e804adx16cf5c4118e'.format(front_url)
    data = {
        "pageSize": 100,
        "take": 100,
        "skip": 3000,
        "page": page_id,
        "sort": [{
            "field": "name",
            "dir": "desc"
        }, {
            "dir": "asc",
            "field": "createdStamp"
        }],
        "bindVars": {},
        "group": [],
        "criteriaStr": "statusEnum != 'I'"
    }
    json_data = s.post(url, json=data).json().get('data')
    return (i.get('id') for i in json_data)


n = 3001
for i in range(31, 100):
    ids = get_goods_by_page_id(i)
    for j in list(ids):
        update_goods_name(j, n)
        n += 1


def get_goods_by_page(page):
    """
    根据页码返回商品ids
    :return: [716088021876753, 716088021876754]
    """
    url = '{}/data/grid/StockCountDetail.list?extendProduct=true&pageSize=50&take=50&skip=6050&page={}&sort%5B0%5D%5Bfield%5D=id&sort%5B0%5D%5Bdir%5D=asc&filter=&aggregate=&loadMore=&criteriaStr' \
          '=masterVoucherId%3D715982124089344&user_req_id=e33e804adx16cf5b2eaa6'.format(front_url, page)
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
    json_r = s.post(url, json=goods_ids).json()
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

# ids = get_goods_ids(3000)
# n = 1
# for i in ids:
#     print(n)
#     # pdd_id = add_goods_to_pdd(i)
#     # add_price(pdd_id)
#     update_goods_name(i, n)
#     n += 1
#     sleep(0.3)

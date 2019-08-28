#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-26 16:08

from time import sleep
import requests
import urllib3

urllib3.disable_warnings()

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhN2Q0NzZhMC1mYmNiLTRmMTItOGRjMC1lYTRmYWMzMWQ1OTQiLCJpYXQiOjE1NjY4MDY3MjF9.LBABPFEJm0nZera2NIisFX74azVs-gXWoh4D9VEUu04'
}


def token():
    url = 'https://inte-cloud.chanjet.com/hsy/u2s7pb1mp9ft/prbhalwfgx/entities/Product/blank?options%5BproductCategoryCode%5D=00&user_req_id=e33e804adx16cccf97d5e'

    r = requests.get(url, headers=headers, verify=False).json()
    return r.get('txnToken')


def create_goods(i):
    url = 'https://inte-cloud.chanjet.com/hsy/u2s7pb1mp9ft/prbhalwfgx/entity/Product?user_req_id=e33e804adx16cccf79de2'
    data = {
        "productTypeId": 100001,
        "taxRate": 0,
        "isMultiSpecEnabled": False,
        "statusEnum": "A",
        "createdUserId": 61000385709,
        "createdStamp": 1566806823393,
        "lastUpdatedStamp": 1566806823393,
        "name": "性能测试UI",
        "valuationMethodEnum": "MOVING_AVG",
        "baseUomId": 706994633965796,
        "salesUomId": 706994633965796,
        "purchaseUomId": 706994633965796,
        "inventoryUomId": 706994633965796,
        "isPurchasable": True,
        "isSalable": True,
        "isMultiUomEnabled": False,
        "productUomGroup": [],
        "lotCtrlEnabled": False,
        "lotExpCtrlEnabled": False,
        "shelfLifeUomEnum": "DAY",
        "priceBaseComp": [{
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
            "isBaseUom": True,
            "editFlag": "new",
            "sequenceNum": 0
        }],
        "productCategoryCode": "00",
        "txnToken": token()
    }
    r = requests.post(url, json=data, headers=headers, verify=False).json()
    print('创建第%s个商品<%s>创建成功,id<%s>' % (i, r.get('name'), r.get('id')))


for i in range(5000):
    create_goods(i + 1)
    sleep(0.5)

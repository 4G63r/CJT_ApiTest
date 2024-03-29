#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-23 14:05

import requests
import urllib3

urllib3.disable_warnings()

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                     '.eyJqdGkiOiJiNDc3ZGY2Yy1kNDE5LTQyNDYtOGNhNi1iZWM5ZmI4NmNkMGEiLCJpYXQiOjE1NjY1Mzk5MzF9'
                     '.aSgvubG6x7k3mCirh2DSqp7aSBKV3woP_03tK_aVUtg',
}


def get_token():
    """创建商品空白页"""
    url = 'https://inte-cloud.chanjet.com/hsy/u2s7pb1mp9ft/4kujod4n6p/entities/Product/blank?options' \
          '%5BproductCategoryCode%5D=00&user_req_id=e33e804adx16cbd136651 '
    r = requests.get(url, headers=headers, verify=False).json()
    return r.get('txnToken')


def run_test():
    url = 'https://inte-cloud.chanjet.com/hsy/u2s7pb1mp9ft/4kujod4n6p/entity/Product?user_req_id=e33e804adx16cbd1fc0c0'
    data = {
        "productTypeId": 100001,
        "taxRate": 0,
        "isMultiSpecEnabled": False,
        "statusEnum": "A",
        "createdUserId": 61000385709,
        "createdStamp": 1566545150837,
        "lastUpdatedStamp": 1566545150838,
        "parentId": 703490074869770,
        "name": "测试图片",
        "valuationMethodEnum": "MOVING_AVG",
        "baseUomId": 703485511467010,
        "salesUomId": 703485511467010,
        "purchaseUomId": 703485511467010,
        "inventoryUomId": 703485511467010,
        "isPurchasable": True,
        "isMadeBySelf": False,
        "isSalable": True,
        "isConsumedByProd": False,
        "isMultiUomEnabled": False,
        "productUomGroup": [],
        "lotCtrlEnabled": False,
        "lotExpCtrlEnabled": False,
        "shelfLifeUomEnum": "DAY",
        "priceBaseComp": [{
            "retailPrice": None,
            "stdWholesalePrice": None,
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
            "editFlag": "new",
            "sequenceNum": 0
        }],
        "productCategoryCode": "00",
        "primaryImageList": [{
            "sequenceNum": 0,
            "image": {
                "url": "https://inte-cloudsto.static.chanjet.com/90001115158/2019/7/23/hsy-1566544733886-hsq.jpeg",
                "size": 19318
            }
        }],
        "txnToken": get_token()
    }

    r = requests.post(url, headers=headers, verify=False, json=data)
    return r.status_code


for i in range(1):
    run_test()
    print('成功添加第%s个商品图片' % (i + 1))

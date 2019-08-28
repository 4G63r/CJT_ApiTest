#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-21 13:43

import sys
import os
import datetime

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.dirname(curPath)
sys.path.append(rootPath)

from common.login import Login
from business.goods import Goods

login = Login()
front_url = login.url
s = login.session

g = Goods(front_url, s)

url_init = '{}/data/grid/GoodsIssue.voucher?user_req_id=e33e804adx16cb75e4428'.format(front_url)
init_data = {
    "pageSize": 50,
    "take": 50,
    "skip": 0,
    "page": 1,
    "sort": [],
    "bindVars": {},
    "group": [],
    "criteriaStr": "bizDate >= DATE(20190823) AND bizDate < DATE_ADD(DATE('20190822'),INTERVAL 1 DAY) AND SYSDATE() > "
                   "0 AND redBlueFlagEnum='BLUE'",
    "havingStr": ""
}
r = s.post(url_init, json=init_data)
print(r)
total_num = r.get('total')  # 记录开始数量

RUN_TIMES = 5000  # 执行次数


def test_1():
    # urllib3.disable_warnings()
    txn_token = g.token

    url = 'https://inte-cloud.chanjet.com/cc/u5ik3iphbm4y/rvotwvgcwv/voucher/GoodsIssue?user_req_id' \
          '=e33e804adx16cb7350814'
    data = {
        "data": {
            "bizDate": 1566810406662,
            "redBlueFlagEnum": "BLUE",
            "soldToCustId": 707048992145414,
            "warehouseId": 707049262809142,
            "bizEmployeeId": 694184894136321,
            "departmentId": 694184894136320,
            "refBoName": None,
            "refVoucherCode": None,
            "srcSalesOrderId": None,
            "dueDate": 1566777600000,
            "paymentTermsEnum": "PREPAY_ALL",
            "billToCustId": 707048992145414,
            "noteTypeEnum": "NORMORL_INVOICE",
            "voucherEntrySourceEnum": "NORMAL",
            "totalAmountWithTax": 10,
            "promoList": [],
            "totalPromoDiscount": 0,
            "totalNetAmountWithTax": 10,
            "shipMethodEnum": "OTHER",
            "isStockOutImmediate": None,
            "exchangeRate": 1,
            "paymentList": [{
                "amount": 10,
                "finAccountId": 703752339062821,
                "paymentMethodTypeId": 703752339062824,
                "salesCollectionTypeEnum": "IMMEDIATE_PAYMENT",
                "uuid": "2",
                "editFlag": "new"
            }],
            "paymentCollectMethodEnum": "RECORD_PAYMENT_INFO",
            "attachmentList": [],
            "bizTypeId": 100011,
            "txnToken": "d4XrWtsiCLKvDy+UMIsnCG23U2B0F2iE9N3rTLF9VGQLZcVqHRWT/eaNaifClNiwE/2jmiFey1o=",
            "isCustChargedFee": None,
            "goodsItems": [{
                "warehouseId": 707049262809142,
                "itemBarcode": "",
                "productId": 706963629670400,
                "transUomId": 703752336310496,
                "transQty": 1,
                "hierarchyPkgQtysText": "1个",
                "baseUomId": 703752336310496,
                "baseQty": 1,
                "availQty": 0,
                "availQtyHierarchyPkgText": "-",
                "onHandQty": 0,
                "onHandQtyHierarchyPkgText": "-",
                "listPrice": 10,
                "netDiscountPct": 1,
                "netPriceWithoutTax": 10,
                "netPriceWithTax": 10,
                "taxPct": 0,
                "netAmountWithoutTax": 10,
                "netTax": 0,
                "netAmountWithTax": 10,
                "netDiscount": 0,
                "priceWithoutTax": 10,
                "priceWithTax": 10,
                "amountWithoutTax": 10,
                "amountWithTax": 10,
                "isFreeGift": False,
                "refBoName": None,
                "refVoucherCode": None,
                "srcSalesOrderId": None,
                "costPrice": 20,
                "costAmount": 20,
                "promoDiscount": 0,
                "extraDiscount": 0,
                "trans2ToTransRate": None,
                "trans2ToBaseRate": None,
                "transToBaseRate": 1,
                "tax": 0,
                "availQtyErrorMsgs": [],
                "commonErrorMsgs": [],
                "priceErrorMsgs": [],
                "sequenceNum": 0,
                "refVoucherId": None,
                "srcSalesOrderCode": None,
                "refDetailBoName": None,
                "trans2ToAuxRate": None,
                "auxToBaseRate": None,
                "isTransToBaseFloating": False,
                "manualInputFlag": 536883201,
                "hierarchyPkgQtys": {},
                "refVoucherDetailId": None,
                "isListPriceIncludingTax": True,
                "transToAuxRate": None,
                "netManualInputFlag": 536883201,
                "discountPct": 1,
                "discount": 0,
                "netStdPriceFlagEnum": "PRICE_WITH_TAX",
                "refNetDiscount": 0,
                "vGrossMargin": -10,
                "vGrossMarginPct": -1,
                "uuid": "1",
                "editFlag": "new"
            }]
        },
        "params": {
            "ignoreWarn": True
        }
    }
    json_r = s.post(url, json=data).json()
    id_ = json_r.get('id')
    return id_


time_s = datetime.datetime.now()
for i in range(RUN_TIMES):
    i_d = test_1()
    total_num += 1
    print('成功创建第<%s>个销货单，id<%s>' % (total_num, i_d))
    # print('成功创建销货单，id<%s>' % i_d)
    # sleep(0.3)
time_e = datetime.datetime.now()
print('创建%s条数据共耗时%s秒' % (RUN_TIMES, round((time_e - time_s).total_seconds(), 1)))

# if __name__ == '__main__':
#     import multiprocessing
#
#     if __name__ == "__main__":
#         pool = multiprocessing.Pool(processes=2)
#         for j in range(10):
#             msg = "hello %s" % (j)
#             pool.apply_async(test_2, (msg,))
#         pool.close()
#         pool.join()
#         print("Sub-process(es) done.")

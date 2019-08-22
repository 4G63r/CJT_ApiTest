#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-21 13:43

# import urllib3
from time import sleep
import datetime
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
    "criteriaStr": "bizDate >= DATE(20190822) AND bizDate < DATE_ADD(DATE('20190822'),INTERVAL 1 DAY) AND SYSDATE() > "
                   "0 AND redBlueFlagEnum='BLUE'",
    "havingStr": ""
}
r = s.post(url_init, json=init_data).json()
total_num = r.get('total')  # 记录开始数量

RUN_TIMES = 1000  # 执行次数


def test_1():
    # urllib3.disable_warnings()
    txn_token = g.token

    url = 'https://inte-cloud.chanjet.com/cc/u5ik3iphbm4y/rvotwvgcwv/voucher/GoodsIssue?user_req_id' \
          '=e33e804adx16cb7350814'
    data = {
        "data": {
            "bizDate": 1566441212158,
            "redBlueFlagEnum": "BLUE",
            "soldToCustId": 701354939252737,
            "warehouseId": 701301657042944,
            "bizEmployeeId": 691651266084867,
            "refBoName": None,
            "departmentId": 691651266084866,
            "refVoucherCode": None,
            "srcSalesOrderId": None,
            "dueDate": 1566432000000,
            "paymentTermsEnum": "PREPAY_ALL",
            "billToCustId": 701354939252737,
            "noteTypeEnum": "NORMORL_INVOICE",
            "voucherEntrySourceEnum": "NORMAL",
            "totalAmountWithTax": 0,
            "promoList": [],
            "totalPromoDiscount": 0,
            "totalNetAmountWithTax": 0,
            "shipMethodEnum": "OTHER",
            "isStockOutImmediate": None,
            "exchangeRate": 1,
            "paymentList": [],
            "paymentCollectMethodEnum": "ON_CREDIT",
            "attachmentList": [],
            "bizTypeId": 100011,
            "txnToken": txn_token,
            "isCustChargedFee": None,
            "goodsItems": [{
                "warehouseId": 701301657042944,
                "itemBarcode": "",
                "productId": 701398425796608,
                "transUomId": 691651265954015,
                "transQty": 1,
                "hierarchyPkgQtysText": "1个",
                "baseUomId": 691651265954015,
                "baseQty": 1,
                "availQty": -1,
                "availQtyHierarchyPkgText": "-1个",
                "onHandQty": -1,
                "onHandQtyHierarchyPkgText": "-1个",
                "listPrice": 0,
                "netDiscountPct": 1,
                "netPriceWithoutTax": 0,
                "netPriceWithTax": 0,
                "taxPct": 0,
                "netAmountWithoutTax": 0,
                "netTax": 0,
                "netAmountWithTax": 0,
                "netDiscount": 0,
                "priceWithoutTax": 0,
                "priceWithTax": 0,
                "amountWithoutTax": 0,
                "amountWithTax": 0,
                "isFreeGift": False,
                "refBoName": None,
                "refVoucherCode": None,
                "srcSalesOrderId": None,
                "costPrice": 1.34,
                "costAmount": 1.34,
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
                "manualInputFlag": 536875009,
                "hierarchyPkgQtys": {},
                "refVoucherDetailId": None,
                "isListPriceIncludingTax": False,
                "transToAuxRate": None,
                "netManualInputFlag": 536883201,
                "discountPct": 1,
                "discount": 0,
                "netStdPriceFlagEnum": "PRICE_WITHOUT_TAX",
                "refNetDiscount": 0,
                "vGrossMargin": -1.34,
                "vGrossMarginPct": None,
                "uuid": "1",
                "editFlag": "new"
            }, {
                "warehouseId": 701301657042944,
                "itemBarcode": "",
                "productId": 701398425796609,
                "transUomId": 691651265954015,
                "transQty": 1,
                "hierarchyPkgQtysText": "1个",
                "baseUomId": 691651265954015,
                "baseQty": 1,
                "availQty": -2,
                "availQtyHierarchyPkgText": "-2个",
                "onHandQty": -2,
                "onHandQtyHierarchyPkgText": "-2个",
                "listPrice": 0,
                "netDiscountPct": 1,
                "netPriceWithoutTax": 0,
                "netPriceWithTax": 0,
                "taxPct": 0,
                "netAmountWithoutTax": 0,
                "netTax": 0,
                "netAmountWithTax": 0,
                "netDiscount": 0,
                "priceWithoutTax": 0,
                "priceWithTax": 0,
                "amountWithoutTax": 0,
                "amountWithTax": 0,
                "isFreeGift": False,
                "refBoName": None,
                "refVoucherCode": None,
                "srcSalesOrderId": None,
                "costPrice": 0,
                "costAmount": 0,
                "trans2ToTransRate": None,
                "trans2ToBaseRate": None,
                "transToBaseRate": 1,
                "tax": 0,
                "availQtyErrorMsgs": [],
                "commonErrorMsgs": [],
                "priceErrorMsgs": [],
                "sequenceNum": 1,
                "refVoucherId": None,
                "srcSalesOrderCode": None,
                "refDetailBoName": None,
                "trans2ToAuxRate": None,
                "auxToBaseRate": None,
                "isTransToBaseFloating": False,
                "manualInputFlag": 536875009,
                "hierarchyPkgQtys": {},
                "refVoucherDetailId": None,
                "isListPriceIncludingTax": False,
                "transToAuxRate": None,
                "netManualInputFlag": 536883201,
                "discountPct": 1,
                "discount": 0,
                "netStdPriceFlagEnum": "PRICE_WITHOUT_TAX",
                "refNetDiscount": 0,
                "vGrossMargin": 0,
                "vGrossMarginPct": None,
                "uuid": "2",
                "editFlag": "new"
            }, {
                "warehouseId": 701301657042944,
                "itemBarcode": "",
                "productId": 701398425796610,
                "transUomId": 691651265954015,
                "transQty": 1,
                "hierarchyPkgQtysText": "1个",
                "baseUomId": 691651265954015,
                "baseQty": 1,
                "availQty": -4,
                "availQtyHierarchyPkgText": "-4个",
                "onHandQty": -4,
                "onHandQtyHierarchyPkgText": "-4个",
                "listPrice": 0,
                "netDiscountPct": 1,
                "netPriceWithoutTax": 0,
                "netPriceWithTax": 0,
                "taxPct": 0,
                "netAmountWithoutTax": 0,
                "netTax": 0,
                "netAmountWithTax": 0,
                "netDiscount": 0,
                "priceWithoutTax": 0,
                "priceWithTax": 0,
                "amountWithoutTax": 0,
                "amountWithTax": 0,
                "isFreeGift": False,
                "refBoName": None,
                "refVoucherCode": None,
                "srcSalesOrderId": None,
                "costPrice": 0,
                "costAmount": 0,
                "trans2ToTransRate": None,
                "trans2ToBaseRate": None,
                "transToBaseRate": 1,
                "tax": 0,
                "availQtyErrorMsgs": [],
                "commonErrorMsgs": [],
                "priceErrorMsgs": [],
                "sequenceNum": 2,
                "refVoucherId": None,
                "srcSalesOrderCode": None,
                "refDetailBoName": None,
                "trans2ToAuxRate": None,
                "auxToBaseRate": None,
                "isTransToBaseFloating": False,
                "manualInputFlag": 536875009,
                "hierarchyPkgQtys": {},
                "refVoucherDetailId": None,
                "isListPriceIncludingTax": False,
                "transToAuxRate": None,
                "netManualInputFlag": 536883201,
                "discountPct": 1,
                "discount": 0,
                "netStdPriceFlagEnum": "PRICE_WITHOUT_TAX",
                "refNetDiscount": 0,
                "vGrossMargin": 0,
                "vGrossMarginPct": None,
                "uuid": "3",
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

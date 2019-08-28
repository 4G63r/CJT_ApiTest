#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-26 19:57

from time import sleep
from common import baseRequest

# ua = 'https://hotfix-cloud.chanjet.com/hsy/uesuexdopqjy/h1pn5f969l'
ua = 'https://hotfix-cloud.chanjet.com/hsy/usidiqxv8d56/tg08auxjqe'
headers = {
    # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkZjI3YzNhZS1lOGUwLTRmNTEtYWI1ZS01YWU0N2E5NmZjZDMiLCJpYXQiOjE1NjY4NzAwMjN9.8B__Od6XyI2iq602lQoG6JwWJofYn82kzJPFOHpsGsg',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMGQzZTM5ZC1mYzYxLTRlZmEtOTljMy05NzE4NjM1ODcwNDgiLCJpYXQiOjE1NjY4ODQ4Mzh9.NxUxItNqhGOOxkC05Dit9PiHito45ua9T58c0IhPKmY'
}


# 统计装饰器
def decorator(func):
    def bb():
        li = [func() for _ in range(10)]
        print(li)
        print('平均值：%s秒' % round(sum(li) / len(li), 2))
        for i in range(len(li)):
            print('第%s次请求的响应时间为%s秒' % (i + 1, li[i]))

    return bb


# 今日日报首页
@decorator
def a1():
    url = '{}/homepage/measureQuery?user_req_id=df8f71ac8x16cd0e0dc53'.format(ua)
    data = [{
        "measures": ["goodsIssueAmount", "goodsIssueCount", "firstTransCustAmount", "firstTransCustCount",
                     "firstTransCustPrice", "oldTransCustCount", "oldTransCustAmount", "oldTransCustPrice",
                     "grossMargin", "salesRevenue", "goodsReturnCount", "goodsReturnAmount", "stockoutAndReciptCount",
                     "agoStockoutAndReciptCount", "replenishedStockoutCount", "replenishedReceiptCount",
                     "stockoutUnreceiptCount", "receiptUnstockoutCount", "unstockoutUnreceiptCount",
                     "totalPaymentApCount", "totalPaymentApAmount", "goodsReceiptAmount", "goodsReceiptCount",
                     "prepaidPaymentArCount", "prepaidPaymentArAmount", "cashPaymentArCount", "cashPaymentArAmount",
                     "arrearsPaymentArCount", "arrearsPaymentArAmount", "totalPaymentArAmount", "totalPaymentArCount",
                     "revenueAmount", "revenueCount", "expenseAmount", "expenseCount", "stockOutAmount",
                     "stockOutCount", "stockInAmount", "stockInCount", "stockTransferCount", "stockCountCount",
                     "stockCountSubCount"],
        "time": "20190827,20190827"
    }]
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 经营流水
@decorator
def jyls():
    url = '{}/data/grid/SummaryOperatingJournal.operation-flow?user_req_id=df8f61f3ax16cd1b6546e'.format(ua)
    data = {
        "pageSize": 0,
        "take": 0,
        "sort": [],
        "bindVars": {
            "v0": "20190801",
            "v1": "20190831"
        },
        "group": [],
        "criteriaStr": "id >= :v0 and id <= :v1"
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 本年
@decorator
def a2():
    url = '{}/homepage/measureQuery?user_req_id=df8f71ac8x16cd0fe4c36'.format(ua)
    data = [{
        "measures": ["goodsIssueAmount", "goodsIssueCount", "firstTransCustAmount", "firstTransCustCount",
                     "firstTransCustPrice", "oldTransCustCount", "oldTransCustAmount", "oldTransCustPrice",
                     "grossMargin", "salesRevenue", "goodsReturnCount", "goodsReturnAmount", "stockoutAndReciptCount",
                     "agoStockoutAndReciptCount", "replenishedStockoutCount", "replenishedReceiptCount",
                     "stockoutUnreceiptCount", "receiptUnstockoutCount", "unstockoutUnreceiptCount",
                     "totalPaymentApCount", "totalPaymentApAmount", "goodsReceiptAmount", "goodsReceiptCount",
                     "prepaidPaymentArCount", "prepaidPaymentArAmount", "cashPaymentArCount", "cashPaymentArAmount",
                     "arrearsPaymentArCount", "arrearsPaymentArAmount", "totalPaymentArAmount", "totalPaymentArCount",
                     "revenueAmount", "revenueCount", "expenseAmount", "expenseCount", "stockOutAmount",
                     "stockOutCount", "stockInAmount", "stockInCount", "stockTransferCount", "stockCountCount",
                     "stockCountSubCount"],
        "time": "20190101,20191231"
    }]
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 销售情况
@decorator
def a3():
    url = '{}/data/grid/GoodsIssue.voucher?user_req_id=df8f71ac8x16cd11c8014'.format(ua)
    data = {
        "pageSize": 50,
        "take": 50,
        "skip": 0,
        "page": 1,
        "sort": [],
        "bindVars": {},
        "group": [],
        "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY) AND SYSDATE() > 0 AND redBlueFlagEnum='BLUE'",
        "havingStr": ""
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=70)
    return round(r.elapsed.total_seconds(), 2)


# 收货情况
@decorator
def a4():
    url = '{}/data/grid/GoodsReceipt.voucher?user_req_id=df8f71ac8x16cd126926c'.format(ua)
    data = {
        "pageSize": 50,
        "take": 50,
        "skip": 0,
        "page": 1,
        "sort": [],
        "bindVars": {},
        "group": [],
        "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY) AND SYSDATE() > 0",
        "havingStr": ""
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 付款情况
@decorator
def a5():
    url = '{}/data/grid/PaymentAP.voucher?user_req_id=df8f71ac8x16cd1293d3f'.format(ua)
    data = {
        "pageSize": 50,
        "take": 50,
        "skip": 0,
        "page": 1,
        "sort": [],
        "bindVars": {},
        "group": [],
        "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY)",
        "havingStr": ""
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 日常收入
@decorator
def a6():
    url = '{}/data/grid/Revenue.voucher?user_req_id=df8f71ac8x16cd12c392f'.format(ua)
    data = {
        "pageSize": 50,
        "take": 50,
        "skip": 0,
        "page": 1,
        "sort": [],
        "bindVars": {},
        "group": [],
        "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY)",
        "havingStr": ""
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 日常支出
@decorator
def a7():
    url = '{}/data/grid/Expense.voucher?user_req_id=df8f71ac8x16cd12e1a43'.format(ua)
    data = {
        "pageSize": 50,
        "take": 50,
        "skip": 0,
        "page": 1,
        "sort": [],
        "bindVars": {},
        "group": [],
        "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY) AND bizTypeId <> 100332",
        "havingStr": ""
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 其他入库
@decorator
def a8():
    url = '{}/data/grid/StockIn.voucher?user_req_id=df8f71ac8x16cd12ff69c'.format(ua)
    data = {
        "pageSize": 50,
        "take": 50,
        "skip": 0,
        "page": 1,
        "sort": [],
        "bindVars": {},
        "group": [],
        "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY)",
        "havingStr": ""
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


if __name__ == '__main__':
    print('↓开始获取性能指标↓\n')

    a1()

    print('\n↑性能指标获取完成↑')

#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-20 09:32

from common.login import Login

login = Login()
front_url = login.url
s = login.session


def aa():
    url = '{}/homepage/measureQuery?user_req_id=e33e804adx16caca43912'.format(front_url)
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
        "time": "20190820,20190820"
    }]
    r = s.post(url, json=data)
    print(r.text)



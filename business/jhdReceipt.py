#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-23 10:56


class JhdReceipt:
    """销货单历史"""

    def __init__(self, url, session, assertion):
        self.url = url
        self.s = session
        self.assert_ = assertion

    @property
    def token(self):
        url = '{}/voucher/GoodsReceipt/init?user_req_id=e33e804adx16cbddd7f4c'.format(self.url)
        r = self.s.get(url)
        if self.assert_.assert_status_code(r, 200):
            return r.json().get('data').get('txnToken')

    def create_jhd(self):
        url = '{}/voucher/GoodsReceipt?user_req_id=e33e804adx16ccccf15a2'.format(self.url)
        data = {
            "data": {
                "vendorId": 707048992145414,
                "redBlueFlagEnum": "BLUE",
                "warehouseId": 703752338538497,
                "bizDate": "2019-08-26T13:23:03.047Z",
                "bizTypeId": 100101,
                "noteTypeEnum": "NORMORL_INVOICE",
                "dueDate": 1566825783047,
                "totalExtraDiscount": 0,
                "paymentList": [{
                    "salesCollectionTypeEnum": "IMMEDIATE_PAYMENT",
                    "paymentMethodTypeId": 703752339062823,
                    "finAccountId": 703752339062820,
                    "amount": 10,
                    "editFlag": "new"
                }],
                "totalAmountWithoutTax": 10,
                "totalAmountWithTax": 10,
                "paymentCollectMethodEnum": "RECORD_PAYMENT_INFO",
                "totalNetAmountWithTax": 10,
                "vRefTotalNetAmountWithTax": 10,
                "txnToken": self.token,
                "expenseAllocationTypeEnum": None,
                "expenseNoteTypeEnum": None,
                "expenseVendorId": None,
                "goodsReceiptExpenseList": [],
                "paymentTermsEnum": "PREPAY_ALL",
                "exchangeRate": 1,
                "goodsItems": [{
                    "warehouseId": 703752338538497,
                    "itemBarcode": "",
                    "productId": 706963495452672,
                    "transUomId": 703752336310496,
                    "transQty": 1,
                    "hierarchyPkgQtysText": "1个",
                    "trans2UomId": None,
                    "baseUomId": 703752336310496,
                    "baseQty": 1,
                    "availQty": 1488151,
                    "availQtyHierarchyPkgText": "1488151个",
                    "onHandQty": 1488151,
                    "onHandQtyHierarchyPkgText": "1488151个",
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
                    "costPrice": 10,
                    "costAmount": 10,
                    "isFreeGift": False,
                    "trans2ToTransRate": None,
                    "trans2ToBaseRate": None,
                    "transToBaseRate": 1,
                    "tax": 0,
                    "sequenceNum": 0,
                    "trans2ToAuxRate": None,
                    "auxToBaseRate": None,
                    "isTransToBaseFloating": False,
                    "manualInputFlag": 536879121,
                    "isListPriceIncludingTax": False,
                    "transToAuxRate": None,
                    "priceTypeId": 100002,
                    "netManualInputFlag": 536870929,
                    "discountPct": 1,
                    "discount": 0,
                    "refNetDiscount": 0,
                    "editFlag": "new",
                    "computing": False,
                    "copying": False,
                    "isNeedSyncCustomizedValue": False,
                    "uuid": "10",
                    "extraInWebNetGroup": {
                        "netPriceWithTax": 10,
                        "netPriceWithoutTax": 10,
                        "netAmountWithTax": 10,
                        "netAmountWithoutTax": 10,
                        "netDiscount": 0,
                        "netDiscountPct": 1,
                        "netTax": 0,
                        "listPrice": 10,
                        "taxPct": 0,
                        "netManualInputFlag": 536870929,
                        "netStdPriceFlagEnum": "PRICE_WITHOUT_TAX"
                    }
                }],
                "voucherEntrySourceEnum": "NORMAL",
                "ignoreWarn": True,
                "id": None
            },
            "params": {}
        }
        r = self.s.post(url, json=data)
        if self.assert_.assert_status_code(r, 200):
            print('成功创建进货单，id<%s>' % r.json().get('id'))

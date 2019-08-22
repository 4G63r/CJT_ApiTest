#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-21 19:22


class Goods:
    """商品相关操作"""

    def __init__(self, url, session):
        self.url = url
        self.s = session

    @property
    def token(self):
        url = '{}/entities/Product/blank?user_req_id=e33e804adx16cb3e8e3f7'.format(self.url)
        json_r = self.s.get(url).json()
        return json_r.get('txnToken')

    def get_measure_infos(self):
        """
        获取计量单位信息
        :return: {'米': 691651265954013, '千克': 691651265954014}
        """
        url = '{}/entities/TenantFavoriteUom/list?fields=uomName&query=form.refer&pageSize=&take=&skip=&page=&sort' \
              '=&filter=&aggregate=&criteriaStr=statusEnum+!%3D+%27I%27+AND+(' \
              'statusEnum+%3D+%27A%27)&user_req_id=e33e804adx16cb3f4cb16'.format(self.url)
        json_r = self.s.get(url).json()
        return {i.get('uomName'): i.get('id') for i in json_r}

    def get_measure_id_by_name(self, measure_name):
        """
        通过计量单位名称查询单位id
        :param measure_name:
        :return:
        """
        infos = self.get_measure_infos()
        if measure_name in infos:
            id_ = infos.get(measure_name)
        else:
            print('计量单位<%s>名称不存在' % measure_name)
            id_ = None
        return id_

    def get_goods_infos(self):
        """
        获取全部商品明细
        :return:
        """
        url = '{}/data/referProduct/InventoryQtyDm.referWithoutWarehouse?pageSize=50&take=50&skip=0&page=1&filter' \
              '=&aggregate=&loadMore=&productTypes=&custId=701354939252737&warehouse=701301657042944&criteriaStr' \
              '=isSalable+%3D+True+AND+statusEnum+%3D+%27A%27+AND+statusEnum+%3D+%27A%27&fields%5B%5D=primaryImage' \
              '&fields%5B%5D=refCostPrice&fields%5B%5D=lastPurchasePrice&fields%5B%5D=searchText&recordDuration=True' \
              '&user_req_id=e33e804adx16cb40bb60b'.format(self.url)
        r = self.s.get(url).json().get('data')
        return {i.get('name'): i.get('id') for i in r}

    def create_goods(self, goods_name):
        """
        创建商品 - 尽量不要创建相同名称的商品
        :return:
        """
        url = '{}/entity/Product?user_req_id=e33e804adx16cb3fc8b36'.format(self.url)
        data = {
            "productTypeId": 100001,
            "taxRate": 0,
            "isMultiSpecEnabled": False,
            "statusEnum": "A",
            "createdUserId": 61000385709,
            "createdStamp": 1566387245840,
            "lastUpdatedStamp": 1566387245840,
            "name": goods_name,
            "valuationMethodEnum": "MOVING_AVG",
            "baseUomId": 691651265954015,
            "salesUomId": 691651265954015,
            "purchaseUomId": 691651265954015,
            "inventoryUomId": 691651265954015,
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
                "uomId": 691651265954015,
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
            "txnToken": self.token
        }
        json_r = self.s.post(url, json=data).json()
        if json_r.get('name') == goods_name:
            print('商品<%s>创建成功，id为<%s>' % (goods_name, json_r.get('id')))
        else:
            print('商品<%s>创建失败！' % goods_name)

    def create_goods_goods(self):
        url = '{}/goodsissue/GoodsIssue/ar/findUsableDepositAmount?user_req_id=e33e804adx16cb424d3e9'.format(self.url)
        data = {
            "id": 701411179626496,
            "vendorId": None,
            "srcWebsiteEnum": "DESKTOP",
            "voucherEntrySourceEnum": "NORMAL",
            "ignoreWarn": True,
            "redBlueFlagEnum": "BLUE",
            "currencyId": 100001,
            "billToCustId": 701354939252737,
            "bizDate": 1566316800000,
            "goodsItems": [{
                "id": 701411179626497,
                "editFlag": "old",
                "netAmountWithTax": 0,
                "transQty": 1,
                "masterVoucherId": 701411179626496,
                "srcSalesOrderId": None,
                "transUomId": 691651265954015
            }, {
                "id": 701411179626498,
                "editFlag": "old",
                "netAmountWithTax": 0,
                "transQty": 2,
                "masterVoucherId": 701411179626496,
                "srcSalesOrderId": None,
                "transUomId": 691651265954015
            }, {
                "id": 701411179626499,
                "editFlag": "old",
                "netAmountWithTax": 0,
                "transQty": 4,
                "masterVoucherId": 701411179626496,
                "srcSalesOrderId": None,
                "transUomId": 691651265954015
            }]
        }
        r = self.s.put(url, json=data)
        print(r.status_code)
        return r.text


if __name__ == '__main__':
    p = Goods()
    print(p.get_goods_infos())

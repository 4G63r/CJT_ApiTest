#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-21 18:12


class CustVendor:
    """往来客户业务操作"""

    def __init__(self, url, session):
        self.url = url
        self.s = session

    @property
    def vendor_token(self):
        url = '{}/entities/CustVendor/blank?options%5BprimaryPartyCategoryCode%5D=00&user_req_id=e33e804adx16cb3a9ea10'.format(
            self.url)
        json_r = self.s.get(url).json()
        return json_r.get('txnToken')

    def create_cust_vendor(self, vendor_name):
        """创建往来单位"""
        url = '{}/entity/CustVendor?user_req_id=e33e804adx16cb3b5281c'.format(self.url)
        data = {
            "partyId": None,
            "partyRoleId": None,
            "id": None,
            "tenantId": None,
            "partyTypeId": None,
            "primaryPartyCategoryId": 0,
            "externalId": None,
            "partyRoleTypeId": 100400,
            "partyName": "",
            "description": "",
            "statusEnum": "A",
            "pricingMethodEnum": "PRICING_BY_LEVEL",
            "isPurIncludingTax": False,
            "versionNo": None,
            "createdStamp": 1566382352983,
            "lastUpdatedStamp": 1566382352983,
            "orgUnit": {
                "orgUnitName": vendor_name
            },
            "custVendorContactList": [],
            "paymentTermsEnum": "PREPAY_ALL",
            "billtoCustVendorId": None,
            "searchText": "",
            "billDay": None,
            "dueDays": None,
            "custLabelList": "",
            "primaryPartyCategoryCode": "00",
            "primaryPartyCategoryName": "",
            "primaryContactTelephone": "",
            "primaryContactName": "",
            "arAmount": None,
            "apAmount": None,
            "arPrepaidAmount": None,
            "apPrepaidAmount": None,
            "partyRoleTypeName": "",
            "firstBizDate": "",
            "openingDate": "1514764800000",
            "billingPeriod": 1,
            "billingDay": None,
            "reconciliationDay": 5,
            "reconciliationAddMonths": 1,
            "reconliliationDays": None,
            "paymentDay": 15,
            "paymentAddMonths": 0,
            "paymentDays": None,
            "vReconciliationDate": None,
            "vPaymentDate": None,
            "srcWebsiteEnum": "DESKTOP",
            "vPrimaryContactFullAddress": "",
            "primaryContactProvince": "",
            "primaryContactCity": "",
            "primaryContactDisctrict": "",
            "primaryContactAddress1": "",
            "primaryContactAddress2": "",
            "primaryContactMobile": "",
            "primaryContactEmail": "",
            "primaryContactFax": "",
            "idPartyRole": None,
            "legalRepresentative": "",
            "openingBank": "",
            "taxNo": "",
            "bankAccountNo": "",
            "primaryContactQq": "",
            "primaryContactWechat": "",
            "custVendorProfileList": "",
            "lastContactStamp": None,
            "custGroupLabelList": "",
            "todayCustLabelList": "",
            "fixedDays": None,
            "mshopFirstBizDate": "",
            "lastBizDate": "",
            "txnToken": self.vendor_token
        }
        r = self.s.post(url, json=data)
        if r.json().get('partyName') == vendor_name:
            print('往来单位<%s>创建成功，id为<%s>' % (vendor_name, r.json().get('id')))
        elif r.status_code != 200:
            print('往来单位<%s>创建失败！' % vendor_name)

    def get_party_infos(self):
        """
        查询所有往来单位信息
        :return: {'宋宵测试单位1': 701354939252737}
        """
        url = '{}/data/grid/CustVendor.list?user_req_id=e33e804adx16cb3c780e4'.format(self.url)
        data = {
            "pageSize": 50,
            "take": 50,
            "skip": 0,
            "page": 1,
            "sort": [],
            "bindVars": {},
            "group": [],
            "criteriaStr": "statusEnum != 'I'"
        }
        json_r = self.s.post(url, json=data).json().get('data')
        return {i.get('partyName'): i.get('id') for i in json_r}

    def get_party_id_by_name(self, vendor_name):
        """
        通过单位名称查询往来单位id
        :return:
        """
        parties = self.get_party_infos()
        if vendor_name in parties:
            id_ = parties.get(vendor_name)
        else:
            print('往来单位<%s>名称不存在' % vendor_name)
            id_ = None
        return id_

    def delete_cust_vendor(self, vendor_name):
        """删除往来单位"""

        id_ = self.get_party_id_by_name(vendor_name)
        if id_:
            url = '{}/entity/CustVendor/{}?user_req_id=e33e804adx16cb3c77f60'.format(self.url, id_)
            r = self.s.delete(url)
            if r.status_code == 200:
                print('往来单位<%s>删除成功' % vendor_name)
            else:
                print('往来单位<%s>没有成功删除！' % vendor_name)

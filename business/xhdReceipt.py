#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-22 14:09

from common.login import Login
from utils import timeStampUtil

login = Login()
front_url = login.url
se = login.session


class GoodsSellHistory:
    """销货单历史"""

    # def __init__(self, url, session):
    #     self.url = url
    #     self.s = session
    def __init__(self):
        self.url = front_url
        self.s = se

    def get_sell_ids(self, start_date=None, end_date=None):
        """
        查询所有销货单记录id

        :param start_date: 开始日期 -> 2019-8-1
        :param end_date: 结束日期
        :return: -> [702303727517696, 701411179626496]
        """
        time_stamp = timeStampUtil.date_to_timestamp(start_date, end_date)
        url = '{}/data/grid/GoodsIssue.voucher?user_req_id=e33e804adx16cb7fa4039'.format(self.url)
        init_data = {
            "fields": ["redBlueFlagEnum.value", "srcWebsiteEnum.value"],
            "pageSize": 50,
            "take": 50,
            "skip": 0,
            "page": 1,
            "sort": [{
                "field": "code",
                "dir": "desc"
            }, {
                "field": "bizDate",
                "dir": "desc"
            }],
            "bindVars": {
                "V0": time_stamp[0],
                "V1": time_stamp[1]
            },
            "group": [],
            "criteriaStr": "bizDate >= FROM_UNIXTIME(:V0) AND bizDate <= FROM_UNIXTIME(:V1)",
            "havingStr": ""
        }
        datas = self.s.post(url, json=init_data).json().get('data')
        return [i.get('id') for i in datas]

    def delete_sold_goods_history(self, start_date=None, end_date=None):
        """
        批量删除销货单记录

        :return:
        """
        ids = self.get_sell_ids(start_date, end_date)
        if len(ids) < 1:
            print('没有销货单可供删除')
        else:
            url = '{}/voucher/GoodsIssue/batchdelete?user_req_id=e33e804adx16cb7ef30fd'.format(self.url)
            json_r = self.s.post(url, json=ids).json()
            delete_count = json_r.get('successCount')
            if len(ids) == delete_count:
                print('成功删除%s个销货单%s' % (delete_count, ids))


if __name__ == '__main__':
    g = GoodsSellHistory()
    print(g.delete_sold_goods_history('2019-8-1', '2019-9-2'))

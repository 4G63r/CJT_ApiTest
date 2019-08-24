#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-23 10:56

from common.login import Login
from common import assertion

login = Login()
front_url = login.url
s = login.session


class JhdReceipt:
    """销货单历史"""

    # def __init__(self, url, session, assertion):
    #     self.url = url
    #     self.s = session
    #     self.assert_ = assertion

    def __init__(self):
        self.url = front_url
        self.s = s
        self.assert_ = assertion

    @property
    def token(self):
        url = '{}/voucher/GoodsReceipt/init?user_req_id=e33e804adx16cbddd7f4c'.format(self.url)
        r = self.s.get(url)
        if assertion.assert_status_code(r):
            token = r.json().get('data').get('txnToken')
        else:
            token = None
        return token


if __name__ == '__main__':
    g = JhdReceipt()
    print(g.token)

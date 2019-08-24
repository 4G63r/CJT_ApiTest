#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-22 18:28

import re
from utils import get_conf_value
from common import baseRequest


class AA:
    @property
    def auth_code(self):
        url = 'https://inte-cia.chanapp.chanjet.com/internal_api/authorizeByJsonp?client_id=4cb832be-e503-4075-9903' \
              '-6aa8d9e29104&callback=jQuery111309092522985477731_1566554809509&jsonp=true'
        r = baseRequest.base_request('get', url)
        print(r.cookies)
        jq_id = r.text.split('(')[0]
        auth_code = re.findall(':"(.+?)"', r.text)[0]
        return jq_id, auth_code

    def see(self):
        url = 'https://inte-cia.chanapp.chanjet.com/internal_api/authorizeByJsonp?client_id=4cb832be-e503-4075-9903' \
              '-6aa8d9e29104&callback=jQuery111309092522985477731_1566554809509&jsonp=true'
        h = {
            'Cookie': 'CIC=512983e300e944fcabc88c2dc0210d03; 93fd6fe240b1591d_gr_cs1=61000385709; 93fd6fe240b1591d_gr_last_sent_cs1=61000385709; 93fd6fe240b1591d_gr_last_sent_sid_with_cs1=fedad6ba-1e69-4de4-84ca-4f57d8eed872; 93fd6fe240b1591d_gr_session_id=fedad6ba-1e69-4de4-84ca-4f57d8eed872; 93fd6fe240b1591d_gr_session_id_fedad6ba-1e69-4de4-84ca-4f57d8eed872=true; Hm_lpvt_338fa58da093fe8c8cfbbcb1b1ca9854=1566558169; Hm_lvt_338fa58da093fe8c8cfbbcb1b1ca9854=1566266457,1566351306,1566440208,1566524925; gr_user_id=6bec0161-0ac2-44b9-a8f7-8c3a476b0fa9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216be064bf2b560-0691e2c74f8e098-491b3700-1764000-16be064bf2c1342%22%2C%22%24device_id%22%3A%2216be064bf2b560-0691e2c74f8e098-491b3700-1764000-16be064bf2c1342%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; a67763d96181ad27_gr_cs1=60012635791; a67763d96181ad27_gr_last_sent_cs1=60012635791; cid=da49ee8ca0aa99dca62740ebf9a14946; UM_distinctid=16cb9d63c0d4cc-001e883c8545678-49183400-1aeaa0-16cb9d63c0eb1e; grwng_uid=18e0b8de-c9d5-4e53-8000-353a55ae5d64; acw_tc=7b39759815646244572514160e778b0b11716e06a77cbfb082d9624d9bfcfe; BIGDATAID=rBAmA10m+hU1exDGAwebAg=='
        }
        r = baseRequest.session_('get', url, headers=h)

        return r

    def bb(self):
        account = get_conf_value.get_account_info()
        un = account.get('username')
        md5_pd = account.get('password')
        url = 'https://inte-passport.chanjet.com/loginV2/webLogin?callback={}&auth_username={}&password={}&auth_code={}&jsonp=1&_=1566554809513'.format(
            self.auth_code[0], un, md5_pd, self.auth_code[1])
        r = baseRequest.base_request('get', url)
        print(r.text)

    def cc(self):
        url = 'https://inte-cia.chanapp.chanjet.com/internal_api/authorizeByJsonp?client_id=93402bb6-4d77-48b9-98e9-88d3c1e246a1&callback=jQuery111309092522985477731_1566554809509&jsonp=true'
        # h = {
        #     'Cookie': 'CIC=512983e300e944fcabc88c2dc0210d03; 93fd6fe240b1591d_gr_cs1=61000385709; 93fd6fe240b1591d_gr_last_sent_cs1=61000385709; 93fd6fe240b1591d_gr_last_sent_sid_with_cs1=fedad6ba-1e69-4de4-84ca-4f57d8eed872; 93fd6fe240b1591d_gr_session_id=fedad6ba-1e69-4de4-84ca-4f57d8eed872; 93fd6fe240b1591d_gr_session_id_fedad6ba-1e69-4de4-84ca-4f57d8eed872=true; Hm_lpvt_338fa58da093fe8c8cfbbcb1b1ca9854=1566558169; Hm_lvt_338fa58da093fe8c8cfbbcb1b1ca9854=1566266457,1566351306,1566440208,1566524925; gr_user_id=6bec0161-0ac2-44b9-a8f7-8c3a476b0fa9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216be064bf2b560-0691e2c74f8e098-491b3700-1764000-16be064bf2c1342%22%2C%22%24device_id%22%3A%2216be064bf2b560-0691e2c74f8e098-491b3700-1764000-16be064bf2c1342%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; a67763d96181ad27_gr_cs1=60012635791; a67763d96181ad27_gr_last_sent_cs1=60012635791; cid=da49ee8ca0aa99dca62740ebf9a14946; UM_distinctid=16cb9d63c0d4cc-001e883c8545678-49183400-1aeaa0-16cb9d63c0eb1e; grwng_uid=18e0b8de-c9d5-4e53-8000-353a55ae5d64; acw_tc=7b39759815646244572514160e778b0b11716e06a77cbfb082d9624d9bfcfe; BIGDATAID=rBAmA10m+hU1exDGAwebAg=='
        # }
        # r = baseRequest.base_request('get', url, headers=h)
        # print(r.text)
        r = self.see().get(url)
        print(r.text)


a = AA()
# print(a.auth_code)
# print(a.cc())
a.see().
a.cc()

#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-22 23:34

"""
SERVER J
每天只能发送500条
相同内容5分钟内不能重复发送
不同内容10秒内不能连续发送
不同内容一分钟只能发送30条(防止程序出错)

24小时请求接口超过1000次的将被封禁
"""
from common.baseRequest import base_request
import time

tokens = {
    'SCU58060Tcc362d832dee07b390f149a76147a9cb5d5eb24d11c13': 'SONGXIAO',
    'SCU58069Tf503b96e8a1f5f3792c24a5407ba73ae5d5f3ede21abc': 'XIAOLI',
    'SCU58073T976ac35308b187aacb419f7ef78197985d5f4cd940e4d': 'YUXIN'
}


def cur_time():
    return time.strftime('%Y%m%d_%H点%M分%S秒')


def get_name_by_token(token):
    return tokens[token]


data = {
    'text': 'Python代码已更新_%s' % cur_time(),
    'desp': '脚本已更新，请拉取最新代码进行测试！%s' % cur_time()
}

r = tuple(map(lambda x: (base_request('get', 'https://sc.ftqq.com/%s.send' % x, data=data).text, x), tokens))
for i in r:
    if 'success' in i[0]:
        print('Send To %s Success' % get_name_by_token(i[1]))
    else:
        print('Send To %s Fail' % get_name_by_token(i[1]))

#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: songxiao
# @Time: 2019-09-26 15:12

"""
测试用例，测试数据，测试报告，log日志绝对路径
"""

import os
import time

cur_dir = os.path.abspath(os.path.dirname(__file__))
cur_time = time.strftime('%Y%m%d_%H%M%S')

# testdata路径
testdata_abspath = '{}/testdatas.xlsx'.format(cur_dir.replace('conf', 'testdata'))

# testcase路径
testcase_abspath = '{}/testcases.xlsx'.format(cur_dir.replace('conf', 'testcase'))

# report路径
report_abspath = '{}/report_{}.html'.format(cur_dir.replace('conf', 'report'), cur_time)

# log路径
log_abspath = '{}/log_{}.log'.format(cur_dir.replace('conf', 'log'), cur_time)

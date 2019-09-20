#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-22 14:21

import time


def date_to_timestamp(start_date=None, end_date=None):
    """
    时期转换为时间戳

    :param start_date: 开始日期 -> 2019-8-1
    :param end_date: 结束日期 -> 2019-8-2
    :return:
    """

    if start_date is None and end_date is None:
        today_date = time.strftime('%Y-%m-%d')
        s_time = '%s 00:00:00' % today_date
        e_time = '%s 23:59:59' % today_date
    else:
        s_time = '%s 00:00:00' % start_date
        e_time = '%s 23:59:59' % end_date

    s_stamp = time.mktime(time.strptime(s_time, "%Y-%m-%d %H:%M:%S"))
    e_stamp = time.mktime(time.strptime(e_time, "%Y-%m-%d %H:%M:%S"))
    return int(s_stamp), int(e_stamp)


def get_current_timestamp():
    """
    获取当前时间戳
    :return:
    """
    return int(time.time() * 1000)

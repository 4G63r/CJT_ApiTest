#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: songxiao
# @Time: 2019-09-25 22:21

from utils.operaExcel import OperaExcel

o = OperaExcel()


def all_case_data():
    """获取全部cases"""
    all_case_datas = []
    for row in range(2, o.max_row + 1):
        is_run = o.get_cell_value(row, 3)
        if is_run == 1:  # 执行
            all_case_datas.append(o.get_cell_value(row, 4))

    return all_case_datas


# print(all_case_data())
print(len(all_case_data()))
#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: lina
# @Time: 2019-09-25 22:51

import xlrd


# 加载excel数据，以第一列数据为键，保存各行数据
def load_excel_data(filename):
    try:
        datas = {}
        workbook = xlrd.open_workbook(filename)
        for i in range(0, workbook.nsheets):
            sheet = workbook.sheet_by_index(i)
            for j in range(1, sheet.nrows):
                # 每一行的数据在row_data 数组里
                row_data = sheet.row_values(j)
                datas[row_data[0]] = row_data
        return datas
    except Exception as e:
        raise ValueError("加载excel数据出现异常,文件：%s，异常：%s" % (filename, e))


# 加载excel的sheet数据，以第一列数据为键，保存各行数据
def load_excel_data_by_sheet(filename, sheetname):
    try:
        datas = {}
        workbook = xlrd.open_workbook(filename)
        sheet = workbook.sheet_by_name(sheetname)
        for i in range(1, sheet.nrows):
            # 每一行的数据在row_data 数组里
            row_data = sheet.row_values(i)
            datas[row_data[0]] = row_data
        return datas
    except Exception as e:
        raise ValueError("加载excel数据出现异常,文件表：%s，%s，异常：%s" % (filename, sheetname, e))


# 根据关键列data获取sheet里行数据
def get_excel_data_by_key(filename, keydata):
    datas = load_excel_data(filename)
    return datas.get(keydata)


# 根据关键列data获取excel里行数据
def get_sheet_data_by_key(filename, sheetname, keydata):
    datas = load_excel_data(filename, sheetname)
    return datas.get(keydata)

# data = get_excel_data_by_key("data\\testdatas.xlsx","name1")
# print(data[2])

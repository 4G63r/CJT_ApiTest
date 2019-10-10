#!/usr/bin/env python
# -*-coding:utf-8 -*-

# @Author: lina
# @Time: 2019-09-25 22:51

import xlrd
from conf import filePath


class OperaExcel:
    """操作excel"""

    def __init__(self, file_name=None, sheet_id=None):
        if file_name is None:
            self.file_name = filePath.testcase_abspath
            self.sheet_id = 0
        else:
            self.file_name = file_name
            self.sheet_id = sheet_id

        self.wb = xlrd.open_workbook(self.file_name)
        self.data = self.get_data()

        # self.wb_case_sh = self.wb[file_sheet]
        # sheet_names = self.wb.sheetnames

    # 获取sheets的内容
    def get_data(self):
        tables = self.wb.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


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


# print(data[2])
file_name = filePath.testcase_abspath
data = get_excel_data_by_key(file_name,"name1")
print(data)
#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-23 18:49

import os
from openpyxl import load_workbook

curPath = os.path.abspath(os.path.dirname(__file__))
case_path = '%s/cases.xlsx' % curPath.replace('utils', 'testcase')


class OperaExcel:
    """操作excel"""

    def __init__(self, file_name=None, sheet_name=None):
        if file_name is None and sheet_name is None:
            file_name = case_path
            sheet_name = 'case_data'
        self.wb = load_workbook(file_name)
        self.ws = self.wb[sheet_name]

    def read_excel(self):
        col = self.ws.max_column
        row = self.ws.max_row
        test_data = ({self.ws.cell(2, j).value: self.ws.cell(i, j).value for j in range(1, col + 1)} for i in
                     range(3, row + 1))
        return test_data

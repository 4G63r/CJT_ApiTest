#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-21 13:43


import subprocess
from conf import filePath

# command = 'pytest'
command = 'pytest -s runTest/caseRunner.py --html={} --self-contained-html'.format(filePath.report_abspath)
r = subprocess.call(command, shell=True)
print(r)

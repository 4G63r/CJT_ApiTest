#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-09-21 15:27

import time
import threading


def func1():
    for i in range(5):
        print("正在做事情1")
        time.sleep(1)


def func2():
    for i in range(6):
        print("正在做事情2")
        time.sleep(1)


# 创建一个线程执行事件1
t1 = threading.Thread(target=func1, name='th_1')
# 创建一个线程执行事件2
t2 = threading.Thread(target=func2, name='th_2')

s = time.time()

print(t1.name)  # 获取线程名

t1.setName('线程1')  # 设置线程名

print(t1.getName())  # 获取线程名

print(t1.isAlive())  # 判断线程是否已执行
# 开始执行线程1
t1.start()
print(t1.isAlive())
# 开始执行线程2
t2.start()

print('当前运行的所有线程对象:', threading.enumerate())  # 当前运行的所有线程对象 []
print('当前运行的线程个数为：', threading.active_count())  # 当前运行的线程个数

# 让主线程等待子线程执行完之后再继续往下执行
t1.join()
t2.join()

e = time.time()
print('耗时%s秒' % (e - s))

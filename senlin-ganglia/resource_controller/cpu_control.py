# -*- coding: UTF-8 -*-
import multiprocessing as mul
import time
import os
import affinity as aff
import signal
import psutil


# 当CPU的使用率没有达到预定的使用率的时候则调用该方法提高CPU的使用率,num为每秒钟的运算次数
def eat_cpu(num):
    while True:
        for i in xrange(0, num):
            continue
        time.sleep(0.01)

if __name__ == "__main__":
    p1 = mul.Process(target=eat_cpu, args=(5000000,))
    p2 = mul.Process(target=eat_cpu, args=(5000000,))
    p3 = mul.Process(target=eat_cpu, args=(5000000,))
    p1.start()
    p2.start()
    p3.start()
    pid1 = p1.pid
    pid2 = p2.pid
    print pid1, "+", pid2
    cpu_num1 = aff.get_process_affinity_mask(pid1)  # 获取CPU的核心值
    print cpu_num1
    aff.set_process_affinity_mask(pid1, 1L)  # 指定程序1运行在CPU的核心1上
    cpu_num2 = aff.get_process_affinity_mask(pid1)
    print cpu_num2
    aff.set_process_affinity_mask(pid2, 2L)  # 指定程序1运行在CPU的核心2上

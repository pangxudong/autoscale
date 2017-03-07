# -*- coding: UTF-8 -*-
import psutil as ps
import time
import os
import ctypes

MEM = None


# 返回系统的内存使用率
def get_system_mem_usage():
    return ps.virtual_memory().percent


# 返回系统的总内存值
def get_system_total_mem():
    return ps.virtual_memory().total/1024/1024


# 剩余的内存还有多少,通过此参数可以计算出所需要增加的内存值为多少
def available_mem():
    return ps.virtual_memory().available


# 内存低于预定的利用率的时候调用该方法增加内存的使用
def eat_mem(number=500):
    # 申请了numberMB的内存
    global MEM
    MEM = ctypes.create_string_buffer(1024*1000*number)


# 内存释放，此函数一般不使用!
def free_mem():
    global MEM
    MEM = None


# rate是期望的利用率,例如期望系统的内存利用率达到60%,rate=60
def main(rate=60):
    time.sleep(1)
    # 并未达到给定的没存使用率
    rest_rate = rate - get_system_mem_usage()
    if rest_rate > 0:
        # 计算出所需要增加的内存值,64是对内存的修正,保证可以超过一点点所需要的内存使用率
        add_mem = int((rest_rate / 100) * get_system_total_mem() + 128)
        print add_mem
        while True:
            if get_system_mem_usage() < rate:
                eat_mem(add_mem)
            time.sleep(1)
            print get_system_mem_usage(), "%"

if __name__ == "__main__":
    try:
        main(70)
        # print ((60 - get_system_mem_usage())/100)*get_system_total_mem()
        # print get_system_total_mem(), "MB"
    except KeyboardInterrupt:
        print "exit..."



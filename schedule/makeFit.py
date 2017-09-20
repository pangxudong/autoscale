#!/usr/bin/python
# -*- coding:utf-8 -*-

from server import *
from asg import *


def first_fit(job_name, job_size):
    global NEXT_FIT_NEXT
    # for one_mem in MEM_ALLO:
    #     if one_mem[MEM_STATE] == 0 and one_mem[MEM_SIZE] > job_size:
    #         break
    #
    #     NEXT_FIT_NEXT = one_mem[MEM_ID] + 1
    #     splitMem(job_name, job_size, one_mem[MEM_ID])


# def init_suffcient(asg_num, server_num):
# def init_insuffcient(asg_num, server_num):

if __name__ == '__main__':
    ASG_NUM = 10
    SERVER_NUM = 100
    asgs = shuffle_asg(ASG_NUM)
    servers = shuffle_server(SERVER_NUM)



    # for server in asgs.get_server_by_status(1):
    #     print server
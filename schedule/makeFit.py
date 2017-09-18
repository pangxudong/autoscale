#!/usr/bin/python
# -*- coding:utf-8 -*-

from server import *
from asg import *
from enum import Enum

import random

SERVER_STATUS = Enum('POWEROFF', 'POWERON', 'DEPLOY', 'RELEASE')

def first_fit(job_name, job_size):
    global NEXT_FIT_NEXT
    # for one_mem in MEM_ALLO:
    #     if one_mem[MEM_STATE] == 0 and one_mem[MEM_SIZE] > job_size:
    #         break
    #
    #     NEXT_FIT_NEXT = one_mem[MEM_ID] + 1
    #     splitMem(job_name, job_size, one_mem[MEM_ID])


def shuffle_server(num):
    servers = []
    for i in range(num):
        status = random.choice(SERVER_STATUS)
        core = random.choice([2, 4, 8, 16])
        servers.append(Server(i, status, core))
    return servers

if __name__ == '__main__':
    SERVER_NUM = 10
    servers = shuffle_server(SERVER_NUM)

    asgs = ASG(1, 1, servers)
    server = Server(1000, 2, 2)

    for server in asgs.get_server_by_status('POWERON'):
        print server
    #
    # asgs.add_server(server)
    # print  asgs
    #
    # asgs.remove_server(server)
    # print  asgs
    #
    # for i in range(SERVER_NUM):
    #     print servers[i]
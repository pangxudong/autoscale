#!/usr/bin/python
# -*- coding:utf-8 -*-
import random

class Server:
    def __init__(self, ID, status, core):
        # status:  0: POWEROFF  1:POWERON 2:DEPLOY 3:RELEASE
        # core: 2GB 4GB 8GB 16GB 32GB
        self.ID = ID
        self.status = status
        self.core = core

    def __str__(self):
        info = ""
        for key in self.__dict__:
            info += key + "=" + str(self.__dict__[key]) + " "
        return "SERVER-" + str(self.ID) + ": " + info

    def get_workload(self):
        return self.core * 10

    def get_performance(self):
        return self.core * 10

def shuffle_server(num):
    # generate <num> of random servers
    servers = []
    for i in range(num):
        status = random.randint(0, 3)
        core = random.choice([2, 4, 8, 16])
        servers.append(Server(i, status, core))
    return servers
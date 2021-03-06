#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import sched
scheduler = sched.scheduler(time.time, time.sleep)

# static
STATUS = {0: "OFF", 1: "ON", 2: "EMPTY"}
PROCESSOR = [2, 4, 8, 16]
ACTION = {0: "POWEROFF", 1: "POWERON", 2: "DEPLOY", 3: "RELEASE"}


class Server:
    def __init__(self, ID, status, core):
        # action:  0: POWEROFF  1:POWERON 2:DEPLOY 3:RELEASE
        # status: on  off empty
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

    def change_status(self, status):
        self.status = status

    def do_poweron(self):
        print "poweron..."+str(self.ID)
        scheduler.enter(2, 1, self.change_status, (STATUS[1], ))
        scheduler.run()

    def do_poweroff(self):
        print "poweroff..."+str(self.ID)
        scheduler.enter(2, 1, self.change_status, (STATUS[0],))
        scheduler.run()

    def do_deploy(self):
        print "deploying..."

    def do_release(self):
        print "releasing..."


def shuffle_server(num):
    # generate <num> of random servers
    servers = []
    for i in range(num):
        status = random.randint(0, len(STATUS))
        core = random.choice(PROCESSOR)
        servers.append(Server(i, status, core))
    return servers

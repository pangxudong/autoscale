#!/usr/bin/python
# -*- coding:utf-8 -*-


class ASG:
    def __init__(self, ID, type, core):
        self.ID = ID
        self.status = status
        self.core = core

    def __str__(self):
        info = ""
        for key in self.__dict__:
            info += key + "=" + str(self.__dict__[key]) + " "
        return "ASG-" + str(self.ID) + ": " + info

#!/usr/bin/python
#-*- coding:utf-8 -*-


class Server:
	def __init__(self, ID, status, core):
		self.ID = ID
		self.status = status
		self.core = core

	def __str__(self):
		info = ""
		for key in self.__dict__:
			info += key + "=" + str(self.__dict__[key]) + " "
		return "SERVER-"+str(self.ID)+": " + info

	def get_workload(self):
		return self.core*10

	def get_performance(self):
		return self.core*10

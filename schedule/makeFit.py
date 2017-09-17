#!/usr/bin/python
#-*- coding:utf-8 -*-

from server import *

def first_fit(job_name, job_size):
	global NEXT_FIT_NEXT
	for one_mem in MEM_ALLO:
		if one_mem[MEM_STATE] == 0 and one_mem[MEM_SIZE] > job_size:
			break

		NEXT_FIT_NEXT = one_mem[MEM_ID] + 1
		splitMem(job_name, job_size, one_mem[MEM_ID])


if __name__ == '__main__':
	# server = Server("fsadkfdaf", "ACTIVE", 8)
	server = []
	for i in range(10):
		server.append(Server(i, "RELEASED", 8))
	
	for i in range(10):
		print server[i]
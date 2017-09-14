#!/usr/bin/python
#-*- coding:utf-8 -*-

class Monitor(object):
	"""docstring for Monitor"""
	# bytes_total, , , vnf_reponse
	# disk: GB 		disk_usage
	# mem: 	GB  	mem_usage
	# net: 	mbps 	net_speed
	# cpu: 			
	# web: 	mbps 	web check, vnf reponse relay
	def __init__(self, disk, mem, net, cpu, web):
		super(Monitor, self).__init__()
		self.items = {}
		if disk is not None:
			self.items.update({"disk":disk})
		if mem is not None:
			self.items.update({"mem":mem})
		if net is not None:
			self.items.update({"net":net})
		if cpu is not None:
			self.items.update({"cpu":cpu})
		if web is not None:
			self.items.update({"web":web})

	def get_items(self):
		return self.items



# workload计算其实要根据需求类型，是计算密集型还是IO密集型。优先级不一样，这里简化了模型
def get_workload(monitor):
	# weight 各项性能指标的 优先级
	weight = {"disk":1, "mem":0.8, "net":0.4, "cpu":0.2, "web":0.3}

	workload = 0
	items = monitor.get_items()
	for key in items:
		workload += items[key] * weight[key]

	return workload

# 一台 标准裸机 所能承受的最大负载
def get_single_max_workload():
	# 标准裸机 配置
	# disk: GB
	# mem: GB
	# net: Mbps
	# cpu: 
	# web: mbps
	performance = {"disk": 1000, "mem":64, "net":100, "cpu":24, "web":40}

	monitor = Monitor(disk = performance["disk"], mem=performance["mem"], net=performance["net"], 
		cpu=performance["cpu"], web=performance["web"])

	return get_workload(monitor)


# 把workload转换成对应所需的 标准裸机 数量
def get_baremetal_num(workload):
	single_max = get_single_max_workload()
	return int(workload/single_max) + 1;



class Preditor(object):
	"""docstring for preditor"""
	# methods: get_predict do_predict 
	def __init__(self, arg):
		super(Preditor, self).__init__()
		self.arg = arg
		


# workload的时间序列
def preditor(sample_workloads):
	return sample_workloads


if __name__ == '__main__':
	monitor = Monitor(disk=1500, mem=70, net=10, cpu=10, web=60)
	workload = get_workload(monitor)
	print get_baremetal_num(workload)
	
	



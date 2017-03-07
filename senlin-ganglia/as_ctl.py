#!/usr/bin/python
from time import sleep
import json, urllib,sys
import subprocess

jsonurl = "http://172.16.13.128:8088/ganglia/api/v2/metrics?cluster=senlin&host=172.16.13.154&metric=cpu_idle"
scale_out_cmd = "curl -X POST http://172.16.13.128:8778/v1/webhooks/1fd0387f-be42-41ab-a246-ccdd6dafb3bc/trigger?V=1"

count = 0
while(True):
	response = urllib.urlopen(jsonurl)
	cpu_free = json.loads(response.read())['metrics'][0]['value']
	print 100-cpu_free
	if (cpu_free < 5):
		count=count+1
		if (count >=11):
			subprocess.Popen(scale_out_cmd, shell=True)
			sys.exit("execute scale_out")
	else:
		count = 0
	sleep(1)


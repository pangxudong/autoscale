## Bare Metal AutoScaling Logic

### Modules
+ Monitor
+ Workload
+ StaticTaskScheduler 
+ Predictor 
+ AutoScalingController

### Monitor Items
+ web_check: OpenStack_hypervisor, vnf_relay
+ bytes_total
+ disk_usage
+ mem_usage

### workload公式
> workload = SUM(zabbix-items * priority）
> metalNums = workload2metal(workload)

### Crontab
+ StaticTaskScheduler： 根据static policy随机配置
+ Predictor： 不断地从zabbix取样本来预测workload曲线
将以上的结果对应转换成baremetal数量的时间图，决策到哪个时刻开始执行scale_in或者scale_out

### 除此之外
如果zabbix监测到持续的workload异常，也要能临时触发scale_in/out来对应。


## Bare Metal AutoScaling Logic

### Modules: 
＋ Workload
＋ StaticTaskScheduler 
＋ Predictor 
＋ autoscalingController

### workload
zabbix-items:
+ bytes_total
+ disk_usage

公式： workload = SUM(zabbix-items * priority）

### 定时任务
+ static policy 随机配置workload
+ predictor 不断地从zabbix取样本来预测workload曲线
将以上的结果对应转换成baremetal数量的时间图，决策到哪个时刻开始执行scale_in或者scale_out

### 除此之外
如果zabbix监测到持续的workload异常，也要能临时触发scale_in/out来对应。


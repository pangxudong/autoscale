## autoscaling group 


## placement group
ref: (https://codingbee.net/tutorials/aws/aws-csa-associate/aws-placement-groups)

AWS terminology: A placement group  is a cluster of instances that are all in the same AZ. These instances have 10 Gbps networks and they  need to have the “Enhanced Networking” feature. 

## placement
ref: http://www.cnblogs.com/07byte/p/5905831.html

虚拟机的调度机制分两个方面:

- placement（放置）: 把虚拟机放在哪个物理机上启动
- migration（迁移）: 从哪个物理机迁移到哪个物理机上


## 调度

## affinity
ref:(http://www.chinacloud.cn/show.aspx?id=23762&cid=12)

Affinity : 多个虚拟机需要放置在相同的主机上
AntiAffinity: 多个虚拟机需要放在在不同的主机上

例如：2个运行database的虚拟机(tier1)和2运行web的虚拟机(tier2)不能同时运行在一台主机上(rack级别上Anti-Affinity,担心单rack单点故障造成所有的database服务器或者web服务器都不可用)。

## workload
ref: (http://www.cnblogs.com/pinganzi/p/7482274.html)

CPU利用率:显示的是程序在运行期间实时占用的CPU百分比

CPU负载:显示的是一段时间内正在使用和等待使用CPU的平均任务数。CPU利用率高，并不意味着负载就一定大。举例来说：如果我有一个程序它需要一直使用cpu的运算功能，那么此时cpu的使用率可能达到100%，但是cpu的工作负载则是趋近于“1”，因为cpu仅负责一个工作嘛！如果同时执行这样的程序两个呢？cpu的使用率还是100%，但是工作负载则变成2了。所以也就是说，当cpu的工作负载越大，代表cpu必须要在不同的工作之间进行频繁的工作切换。

每个内核的负载为1，并不能算是一种理想状态！这意味着我们的CPU一直很忙，不得清闲。网上有说理想的状态是每个内核的负载为0.7左右，我比较赞同，0.7乘以内核数，得出服务器理想的CPU负载。

## Standard Workload Format
ref:  http://www.cs.huji.ac.il/labs/parallel/workload/swf.html

这里是通过所执行job相关的属性对workload进行描述的，下面是本次实验我比较关注的一些属性：
### The Data Fields
5. Number of Allocated Processors -- an integer. In most cases this is also the number of processors the job uses;
6. Average CPU Time Used -- both user and system, in seconds. This is the average over all processors of the CPU time used, and may therefore be **smaller than the wall clock** runtime.

###Header Comments
2. Computer: Brand and model of computer

ps. 我在想是不是通过主机的品牌，结合data fields中的cpu时间，可以判断workload ?

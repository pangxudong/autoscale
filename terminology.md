## 术语解释

### autoscaling group 


### placement group
ref: https://codingbee.net/tutorials/aws/aws-csa-associate/aws-placement-groups

AWS terminology: A placement group  is a cluster of instances that are all in the same AZ. These instances have 10 Gbps networks and they  need to have the “Enhanced Networking” feature. 

### placement
ref: http://www.cnblogs.com/07byte/p/5905831.html

虚拟机的调度机制分两个方面:

- placement（放置）: 把虚拟机放在哪个物理机上启动
- migration（迁移）: 从哪个物理机迁移到哪个物理机上


### 调度

### affinity
ref: http://www.chinacloud.cn/show.aspx?id=23762&cid=12

Affinity : 多个虚拟机需要放置在相同的主机上
AntiAffinity: 多个虚拟机需要放在在不同的主机上

例如：2个运行database的虚拟机(tier1)和2运行web的虚拟机(tier2)不能同时运行在一台主机上(rack级别上Anti-Affinity,担心单rack单点故障造成所有的database服务器或者web服务器都不可用)。

### workload
ref: (http://www.cnblogs.com/pinganzi/p/7482274.html)

CPU利用率:显示的是程序在运行期间实时占用的CPU百分比

CPU负载:显示的是一段时间内正在使用和等待使用CPU的平均任务数。CPU利用率高，并不意味着负载就一定大。举例来说：如果我有一个程序它需要一直使用cpu的运算功能，那么此时cpu的使用率可能达到100%，但是cpu的工作负载则是趋近于“1”，因为cpu仅负责一个工作嘛！如果同时执行这样的程序两个呢？cpu的使用率还是100%，但是工作负载则变成2了。所以也就是说，当cpu的工作负载越大，代表cpu必须要在不同的工作之间进行频繁的工作切换。

每个内核的负载为1，并不能算是一种理想状态！这意味着我们的CPU一直很忙，不得清闲。网上有说理想的状态是每个内核的负载为0.7左右，我比较赞同，0.7乘以内核数，得出服务器理想的CPU负载。

英文解释: CPU workload indicates the number of instructions being executed by the processor during a given period or at a particular instant of time. 

### Standard Workload Format
ref:  http://www.cs.huji.ac.il/labs/parallel/workload/swf.html

这里是通过所执行job相关的属性对workload进行描述的，下面是本次实验我比较关注的一些属性：

The Data Fields <br>
5. Number of Allocated Processors -- an integer. In most cases this is also the number of processors the job uses; <br>
6. Average CPU Time Used -- both user and system, in seconds. This is the average over all processors of the CPU time used, and may therefore be **smaller than the wall clock** runtime.

Header Comments  <br>
2. Computer: Brand and model of computer

ps. 我在想是不是通过主机的品牌，结合data fields中的cpu时间，可以判断workload ?


### DPI 
ref: (http://www.wikiwand.com/zh-sg/%E6%B7%B1%E5%BA%A6%E5%8C%85%E6%A3%80%E6%B5%8B)

深度数据包检测，是一种电脑网络数据包过滤技术，用来检查通过检测点之数据包的数据部分（亦可能包含其标头），以搜索不匹配规范之协议、病毒、垃圾邮件、入侵，或以预定之准则来决定数据包是否可通过或需被路由至其他不同目的地，亦或是为了收集统计数据之目的。IP数据包有许多个标头；正常运作下，网络设备只需要使用第一个标头（IP标头），而使用到第二个标头（TCP、UDP等）则通常会与深度数据包检测相对，而被称之为浅度数据包检测（一般称为状态数据包检测）[1]。


深度数据包检测结合了入侵检测系统（IDS）、入侵预防系统（IPS）及状态防火墙等功能[4]。

流行的实现版本：
- nDPI
- suricata

###  Stateless Network Functions
ref: http://10.3.200.202/cache/13/03/conferences.sigcomm.org/44d5ae6b89335e5eccab0746f632fd9b/p49.pdf

Newly virtualized network functions (like firewalls,
routers, and intrusion detection systems) should be easy
to consume. Despite recent efforts to improve their elasticity
and high availability, network functions continue
to maintain important flow state, requiring traditional
development and deployment life cycles. At the same
time, many cloud-scale applications are being rearchitected
to be stateless by cleanly pushing application
state into dedicated caches or backend stores. This state
separation is enabling these applications to be more
agile and support the so-called continuous deployment
model. In this paper, we propose that network functions
should be similarly redesigned to be stateless. Drawing
insights from different classes of network functions,
we describe how stateless network functions can leverage
recent advances in low-latency network systems to
achieve acceptable performance. Our Click-based prototype
integrates with RAMCloud; using NAT as an
example network function, we demonstrate that we are
able to create stateless network functions that maintain
the desired performance.

个人理解： 

1) 我的小论文中，使用无状态VNF做实验是简化了模型。假如都是有状态的VNF，scale_in时不能直接关机， 而需要先做迁移或持久化处理再关机。

2) 网络功能(NF)处理的对象是网络数据包， 包括单个包的header和负载。 而一般的软件应用的处理单元往往是应用层的数据格式， 对数据包等网络协议栈完全透明。


### 控制平面 数据平面
ref:  http://blog.csdn.net/kkkkkkkooooooo111/article/details/52319901
http://sunyongfeng.com/201706/networks/switch/three_panel.html

高端路由器由控制平面control plane和数据平面data plane（也称为转发平面）组成。每个平面都有自己的CPU和内存。控制平面负责执行路由选择协议，管理路由选择处理必备的数据库信息并生成FIB表（Forward Information Base，转发信息库）.FIB信息将会被转发到用于接收传输分组的数据平面中。控制平面和数据平面分离的优点在于，当需要转发的通信量剧增导致数据平面资源枯竭时，虽然无法继续进行分组转发，但对控制平面上的路由选择处理所涉及的资源没有任何影响。同样，当路由选择处理负载剧增导致控制平面资源枯竭时，也不会给数据平面的资源以及分组转发带来任何影响。


openstack 承载vnf所需提高的一些问题：
5. 高性能数据平面 很多运营商网络的功能（比如深度包检测、媒体网关、会话边界控制器和移动核心服务网关以及分组数据网络网关）目前是基于定制化硬件实现的，为的是获得更高的处理能力和输入输出吞吐量。在商业服务器上以hypervisor运行这些功能会导致10倍的性能下降。
http://www.cnii.com.cn/technology/2015-10/23/content_1640533_3.htm

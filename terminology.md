## autoscaling group


## placement
ref: (https://codingbee.net/tutorials/aws/aws-csa-associate/aws-placement-groups)
(https://quizlet.com/185446688/elastic-cloud-compute-ec2-auto-scaling-configuring-auto-scaling-groups-flash-cards/)


## affinity
ref:(http://www.chinacloud.cn/show.aspx?id=23762&cid=12)

## 调度


## workload
ref: (http://www.cnblogs.com/pinganzi/p/7482274.html)
CPU利用率:显示的是程序在运行期间实时占用的CPU百分比

CPU负载:显示的是一段时间内正在使用和等待使用CPU的平均任务数。CPU利用率高，并不意味着负载就一定大。举例来说：如果我有一个程序它需要一直使用cpu的运算功能，那么此时cpu的使用率可能达到100%，但是cpu的工作负载则是趋近于“1”，因为cpu仅负责一个工作嘛！如果同时执行这样的程序两个呢？cpu的使用率还是100%，但是工作负载则变成2了。所以也就是说，当cpu的工作负载越大，代表cpu必须要在不同的工作之间进行频繁的工作切换。

每个内核的负载为1，并不能算是一种理想状态！这意味着我们的CPU一直很忙，不得清闲。网上有说理想的状态是每个内核的负载为0.7左右，我比较赞同，0.7乘以内核数，得出服务器理想的CPU负载。

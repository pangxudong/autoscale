## 裸机资源动态分配调度器

把裸机资源分配到不同的ASG

### 类似情况
类似情况于操作系统中的**动态分区分配**, 这种分配不预设分区的数目和大小，而是在作业装入内存时，根据作业的大小动态建立分区，使分区大小满足作业的需要。

分区分配算法：
- 首次适应
- 循环首次适应
- 最佳适应
- 最坏适应

ref: https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E5%86%85%E5%AD%98%E5%88%86%E9%85%8D
http://blog.csdn.net/cm_cyj_1116/article/details/53518790


### 数据结构

- Server : ID, coreNum, status, workload
- ASG : workType, serverList
- Job : workType, runTime, (参考standard workload format)

### 基于预测的分配

### 时间序列









### 虚拟机的自动伸缩模型
详细步骤及代码，请参考： 
	魏亮, 黄韬, 陈建亚, 刘韵洁, "基于工作负载预测的虚拟机整合算法", 电子与信息学报， 第35卷，第6期， 2013.6

本人虚拟机调度是 背包问题， 虚拟机的placement有Hosts配置限制。
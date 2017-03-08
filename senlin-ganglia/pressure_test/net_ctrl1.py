# -*- coding:utf-8 -*-
from __future__ import division
import os
import ast


class NetCtrl:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.ip_list = self.ip_address.split(".")
        self.ip_part1 = self.ip_list[0]
        self.ip_part2 = self.ip_list[1]
        self.ip_part3 = self.ip_list[2]
        self.ip_part4 = self.ip_list[3]

    # @return 带宽的大小
    def get_bandwidth(self):
        # print "ip address:%s, port:%s" % (self.ip_address, self.port)
        # print "Test beginning,please wait for 10 seconds..."
        result = os.popen("iperf3 -u -c %s.%s.%s.%s -p %s  -b 10M | grep bits/sec" %
                          (self.ip_part1, self.ip_part2, self.ip_part3, self.ip_part4, self.port)).readlines()
        tmp = result[-1].split()
        bandwidth = tmp[6]
        bandwidthunit = tmp[7]
        temp_list = [bandwidth, bandwidthunit]
        # print "bandwidth：%s%s" % (tmp[6], tmp[7])
        # return bandwidth
        return temp_list

    # @para num:输入想让带宽占用的数值，如果想让带宽占用率为20%,请输入20
    # @para duration_time:想让带宽被占用持续的时间，单位是秒(s)
    def eat_bandwidth(self, num=20, duration_time=10):
        temp = self.get_bandwidth()
        bandwidth = temp[0]
        # print type(bandwidth)
        bandwidth = ast.literal_eval(bandwidth)
        # print bandwidth
        # bandwidth = 7.25
        rate = num/100
        strip_width = rate*bandwidth
        # strip_width = 1.2
        CLI = "iperf3 -u -c %s.%s.%s.%s -p %s -b %.2fM -t %s" % \
              (self.ip_part1, self.ip_part2, self.ip_part3, self.ip_part4, self.port, strip_width, duration_time)
        # print CLI
        result = os.popen(CLI).readlines()
        res1 = result[-5].split()
        res2 = result[-4].split()
        print "%s       %s    %s      %s   %s" % (res1[2], res1[3], res1[4], res1[5], res1[6])
        print "%s%s  %s%s  %s%s  %s%s   %s" % (res2[2], res2[3], res2[4], res2[5], res2[6], res2[7], res2[8],
                                                res2[9], res2[10])

        # print type(res1), "res1:", res1
        # print "res2:", res2
        # print result[-5]
        # print result[-4]
        return strip_width

    def print_bandwidth(self):
        print "ip address:%s, port:%s" % (self.ip_address, self.port)
        print "Test beginning,please wait for 10 seconds..."
        tmp = self.get_bandwidth()
        print "bandwidth：%s%s" % (tmp[0], tmp[-1])


if __name__ == "__main__":
    net = NetCtrl("10.108.125.112", 5201)
    # tmp = net.get_bandwidth()
    # print "bandwidth：%s%s" % (tmp[0], tmp[-1])
    # net.eat_bandwidth()
    # net.print_bandwidth()
    net.eat_bandwidth()

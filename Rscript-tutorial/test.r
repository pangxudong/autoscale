#!/usr/local/bin/Rscript

# read excel file

library(gdata)
names<-read.xls("/Users/yuanxu/Downloads/yingling.xls",sheet=1,header=F)

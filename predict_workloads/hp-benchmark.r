#!/usr/local/bin/Rscript

duration <- c(5,2,30,5)

event <- c("poweron","poweroff","deploy","release")

barplot(duration,names.arg=event,xlab="Events",ylab="Time Costs",col="blue", main="HP Gen9 Benchmark",border="red")
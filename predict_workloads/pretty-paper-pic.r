#!/usr/local/bin/Rscript

week<-c(1,2,3,4,5,6)
x<-c(3,8,19,24,6,1)
y<-c(1,25,21,3,2,1)

lines(week,y,col="green",pch=16,bg="yellow",xlim=c(0,6),ylim=c(0,30),lwd=2,xlab="WEEK",ylab="STUDENT",main="lesson",sub="class",col.main="green",font.main=2,asp=0,cex=1.2,type="b",lty=2);

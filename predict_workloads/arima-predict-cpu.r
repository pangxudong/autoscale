#!/usr/local/bin/Rscript

library(forecast)
rawdata<-read.table("data/cpu.dat")

tsdata = ts(rawdata, frequency=12, start=c(1600,1))

arimadata<-auto.arima(tsdata,trace=T)

forecastdata<-forecast(arimadata, h=12,fan=T)

plot.ts(forecastdata)
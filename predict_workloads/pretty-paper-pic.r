#!/usr/local/bin/Rscript

# ref:  
# http://www.harding.edu/fmccown/r/
# https://plot.ly/r/line-and-scatter/


setwd("/Users/yuanxu/Developer/autoscaling/predict_workloads")

workloads_data <- read.table("data/sample-output.dat", header=T, sep="\t") 

# Compute the largest y value used in the data (or we could
# just use range again)
max_y <- max(workloads_data)

# Define colors to be used for ARIMA, ESM, ACTUAL
plot_colors <- c("blue","red","forestgreen")

# Start PDF device driver to save output to figure.pdf
pdf(file="figure.pdf", bg="white")

# Graph autos using y axis that ranges from 0 to max_y.
# Turn off axes and annotations (axis labels) so we can 
# specify them ourself
plot(workloads_data$ARIMA, type="o", col=plot_colors[1], 
   ylim=c(0,max_y), axes=FALSE, ann=FALSE)

# Make x axis using Mon-Fri labels
# axis(1, at=1:5, lab=c("Mon", "Tue", "Wed", "Thu", "Fri"))
axis(1, at=1:10)

# Make y axis with horizontal labels that display ticks at 
# every 4 marks. 4*0:max_y is equivalent to c(0,4,8,12).
axis(2, las=1, at=4*0:max_y)

# Create box around plot
box()

# Graph ESM with red dashed line and square points
lines(workloads_data$ESM, type="o", pch=22, lty=2, 
   col=plot_colors[2])

# Graph ACTUAL with green dotted line and diamond points
lines(workloads_data$ACTUAL, type="o", pch=23, lty=3, 
   col=plot_colors[3])

# Create a title with a red, bold/italic font
title(main="predict workload vs actual workload", col.main="red", font.main=4)

# Label the x and y axes with dark green text
title(xlab= "Time", col.lab=rgb(0,0.5,0))
title(ylab= "Worloads", col.lab=rgb(0,0.5,0))

# Create a legend at (1, max_y) that is slightly smaller 
# (cex) and uses the same line colors and points used by 
# the actual plots
legend(1, max_y, names(workloads_data), cex=0.8, col=plot_colors, 
   pch=21:23, lty=1:3);
   
# Turn off device driver (to flush output to png)
dev.off()

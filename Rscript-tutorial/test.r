#!/usr/local/bin/Rscript

# read excel file
library(gdata)
library(xlsx)

setwd("/Users/yuanxu/Downloads/")
names<-read.xls("yingling.xls",sheet=1,header=F)


# names is data.frame type
flag = 0
mdmatrix <- matrix(c("",""), nrow=1)
for (i in 1:nrow(names)) {
	for (j in 1:ncol(names[i,])) {
		if (flag == 0) {
			temp = names[i,j]
			flag = 1
		} else {
			row = c(as.character(temp),as.character(names[i,j]))
			mdmatrix <- rbind(mdmatrix, row)
			flag = 0
		}
	}
}

# convert matrix to dataframe
mingdan <- data.frame(mdmatrix)

# write to xls
write.xlsx(mingdan, file="mingdan.xls")
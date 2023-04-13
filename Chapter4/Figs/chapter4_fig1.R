#!/usr/bin/env R

## setwd
setwd("/Users/sl666/Github/phd_thesis/Chapter4/Figs")

## load library
library(ggpubr)
library(ggplot2)
library(gridExtra)
library(data.table)

## data.table
dt = fread("chapter4_fig1_zmw.csv")
dt2 = fread("chapter4_fig1_zmw_ccs_read_length.csv")



ggplot(df, aes(x=x, y=y)) + 
  geom_point() +
  geom_smooth(method="lm", aes(color="Exp Model"), formula= (y ~ exp(x)), se=FALSE, linetype = 1) +
  geom_line(data = log.model.df, aes(x, y, color = "Log Model"), size = 1, linetype = 2) + 
palette = c("#98D7EC","#212121","#FF003A","#A6A6A6","#83A603","#F5ABCC")

o = ggplot(dt, aes(x=zmw, y=cost)) +
  theme_bw() + 
  geom_point(size = 2, color = "#038C73") +
  theme(legend.title = element_blank()) + 
  geom_smooth(method="glm",
              method.args=list(family=gaussian(link="log")),
              se=FALSE,
              size = 1,
              linetype = 1,
              ) + 
  theme(text = element_text(size=12)) + 
  theme(legend.title = element_blank()) +  
  labs(x = "\nNumber of ZMWs per SMRTcell (millions) \n", y = "\nCCS sequencing cost per \n30-fold sequence coverage of a human genome\n") 

 p = ggplot(dt2, aes(x=zmw, y=cost)) +
  theme_bw() + 
  geom_point(size = 2, color = "#F24C3D") +
  theme(legend.title = element_blank()) + 
  geom_smooth(method="glm",
              method.args=list(family=gaussian(link="log")),
              se=FALSE,
              size = 1,
              linetype = 1,
              ) + 
  theme(text = element_text(size=12)) + 
  theme(legend.title = element_blank()) +  
  labs(x = "\nNumber of ZMWs per SMRTcell (millions) \n", y = "\nCCS sequencing cost per \n30-fold sequence coverage of a human genome\n")  

op = ggarrange(o, p, ncol = 2, nrow = 1)
 
## ggsave
ggsave("chapter4_fig1.pdf", op, width = 20, height=10)


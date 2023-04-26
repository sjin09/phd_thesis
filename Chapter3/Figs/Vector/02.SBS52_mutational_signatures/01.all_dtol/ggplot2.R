#!/usr/bin/env R

## library
library(plyr)
library(ggplot2)
library(magrittr)
library(data.table)
library(randomcoloR)
library(RColorBrewer)

## setwd
setwd("/Users/sl666/Github/phd_thesis/Chapter3/Figs/02.som_germ_mutsig/01.all_dtol")

## options
options(scipen = 999)

## import
i = fread("HDP_exposure_all_SBS52.tsv")
j = i[mutsig!="SBS0"]
j = j[order(sample)]
mutsig_lst = unique(j[,mutsig])
j[,mutsig:=factor(mutsig, levels=mutsig_lst)]
sample_lst = unique(j[,sample])
sample_count = length(sample_lst)
sig_count = length(mutsig_lst)
sig_palette = distinctColorPalette(sig_count)

## ggplot2
## pdf("HDP.pdf", height=12, width=25)
for(k in seq(1,998,20)){
  o = ggplot(j[sample %in% sample_lst[k:(k+19)]], aes(x=sample, y=attribution, fill=mutsig)) +
    geom_bar(stat="identity", )  +
    theme_bw() + 
    scale_fill_manual(values = sig_palette) +
    theme(legend.title = element_blank()) +
    labs(x = "\nSample\n", y = "\nMutational Signature Attribution\n") +
    theme(axis.text.x = element_text(angle = 90, hjust = 1), text = element_text(size=12)) 
  ggsave(filename=sprintf("%s.pdf", k), o, height=12, width=25)
}
## dev.off()



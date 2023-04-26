#!/usr/bin/env R

## library
library(plyr)
library(ggplot2)
library(magrittr)
library(data.table)
library(randomcoloR)
library(RColorBrewer)

## setwd
setwd("/Users/sl666/Github/mutsig/02.germline_and_somatic_mutations/01.120423/01.all_dtol")

## options
options(scipen = 999)

## import
i = fread("HDP_exposure_all_SBS52.tsv")
j = i[mutsig!="SBS0"]
mutsig_lst = unique(j[,mutsig])
j[,mutsig:=factor(mutsig, levels=mutsig_lst)]
sample_lst = unique(j[,sample])
sample_count = length(sample_lst)
sig_count = length(mutsig_lst)
sig_palette = distinctColorPalette(sig_count)

## ggplot2
pdf("HDP.pdf", height=12, width=25)
for(i in seq(1,1000,20)){
  o = ggplot(j[sample %in% sample_lst[i:(i+20)]], aes(x=sample, y=attribution, fill=mutsig)) +
    geom_bar(stat="identity", )  +
    theme_bw() + 
    scale_fill_manual(values = sig_palette) +
    theme(legend.title = element_blank()) +
    labs(x = "\nSample\n", y = "\nMutational Signature Attribution\n") +
    theme(axis.text.x = element_text(angle = 90, hjust = 1), text = element_text(size=12)) 
  print(o)
}
dev.off()



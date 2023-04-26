#!/usr/bin/env R

library(ggplot2)
library(pheatmap)
library(d3heatmap)
library(ggcorrplot)
library(data.table)
setwd("/Users/sl666/Github/phd_thesis/Chapter3/R/04.tol96_vs_tol52")

mat = read.table("tol96_in_sbs52_vs_tol52.tsv")
pdf("TOL_SBS96_in_SBS52_vs_TOL_SBS52.pdf", width=10, height=10)
pheatmap(mat)
dev.off()
## ggcorrplot(mat, hc.order=TRUE)

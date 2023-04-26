#!/usr/bin/env R

library(ggplot2)
library(pheatmap)
library(d3heatmap)
library(ggcorrplot)
library(data.table)
setwd("/Users/sl666/Github/phd_thesis/Chapter3/R/01.tol_vs_cosmic")

mat = read.table("tol_vs_cosmic.tsv")
pdf("TOL_vs_TOL.pdf", width=10, height=10)
pheatmap(mat)
dev.off()
## ggcorrplot(mat, hc.order=TRUE)

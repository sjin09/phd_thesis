#!/usr/bin/env python

import numpy as np
from collections import defaultdict

ROOT_DIR="/Users/sl666/Github/phd_thesis/Chapter3/Table/subread_per_ccs_read"

sample2prefix = defaultdict(list)
for line in open("input2.fofn").readlines():
    sample, prefix  = line.strip().split()
    sample2prefix[sample].append(prefix)

for sample, prefix_lst in sample2prefix.items():
    count_lst = []
    ccs_file = "{}/{}/xgPhoLine1.{}.minimap2_ccs.primary_alignments.sorted.qname".format(ROOT_DIR, sample, sample)
    ccs_set = set([line.strip() for line in open(ccs_file).readlines()])
    for prefix in prefix_lst:
        subread_file = "{}/{}/{}.qname_count.txt".format(ROOT_DIR, sample, prefix)
        for l1 in open(subread_file):
            if l1.startswith("qname"):
                continue
            qname, count = l1.strip().split()
            if qname in ccs_set:
                count_lst.append(int(count))
    mean_subread_count = np.mean(count_lst)
    std_subread_count = np.std(count_lst)
    print("sample: {}, mean: {}, std: {}".format(sample, mean_subread_count, std_subread_count))

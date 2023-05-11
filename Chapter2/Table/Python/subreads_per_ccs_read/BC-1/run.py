#!/usr/bin/env python

import numpy as np

ccs_file = "BC-1.ccs_qname.txt"
fofn_file = "input.fofn"
ccs_set = set([line.strip() for line in open(ccs_file).readlines()])

count_lst = []
for l0 in open(fofn_file).readlines():
    p = l0.strip()
    for l1 in open("{}.qname_count.txt".format(p)):
        if l1.startswith("qname"):
            continue
        qname, count = l1.strip().split()
        if qname in ccs_set:
            count_lst.append(int(count))
print("mean:", np.mean(count_lst))
print("std:", np.std(count_lst))

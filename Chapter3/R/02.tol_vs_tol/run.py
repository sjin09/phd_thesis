#!/usr/bin/env python

import natsort
from numpy import dot
from numpy.linalg import norm
from collections import defaultdict
## cos_sim = dot(a, b)/(norm(a)*norm(b))

counter = 0 
tol_sig_hsh = defaultdict(list)
for line in open("dtol_sigs.csv").readlines()[1:]:
    arr = line.strip().split(",")
    for i, j in enumerate(arr):
        if i == 0:
            continue
        tol_sig_hsh[i].append(float(j))

o = open("tol_vs_tol.tsv", "w")
sig_lst = natsort.natsorted([str("SBS{}".format(i)) for i in list(tol_sig_hsh.keys())])
o.write("{}\n".format("\t".join(sig_lst)))
for i, ip in tol_sig_hsh.items():
    sim_lst = [str("SBS{}".format(i))]
    for j, jp in tol_sig_hsh.items():
        sim = str(dot(ip, jp)/(norm(ip)*norm(jp)))
        sim_lst.append(sim)
    o.write("{}\n".format("\t".join(sim_lst))) 
o.close()

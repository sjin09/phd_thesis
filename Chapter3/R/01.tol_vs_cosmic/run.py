#!/usr/bin/env python

import natsort
from numpy import dot
from numpy.linalg import norm
from collections import defaultdict

counter = 0 
tol_sig_hsh = defaultdict(list)
for line in open("dtol_sigs.csv").readlines()[1:]:
    arr = line.strip().split(",")
    for i, j in enumerate(arr):
        if i == 0:
            continue
        tol_sig_hsh[i].append(float(j))

cosmic_sig_hsh = defaultdict(list)
for line in open("sigProfiler_SBS_signatures_2019_05_22.csv").readlines():
    if line.startswith("Type"):
        cosmic_header_lst = line.strip().split(",") 
        cosmic_sig_lst = [i for i in cosmic_header_lst if i.startswith("SBS")]
        continue
    arr = line.strip().split(",")
    for i in cosmic_sig_lst:
        cosmic_sig_hsh[i].append(float(arr[cosmic_header_lst.index(i)]))

o = open("tol_vs_cosmic.tsv", "w")
tol_sig_lst = natsort.natsorted([str("TOL{}".format(i)) for i in list(tol_sig_hsh.keys())])
o.write("{}\n".format("\t".join(cosmic_sig_lst)))
for i, ip in tol_sig_hsh.items():
    sim_lst = [str("TOL{}".format(i))]
    for j, jp in cosmic_sig_hsh.items():
        sim = str(dot(ip, jp)/(norm(ip)*norm(jp)))
        sim_lst.append(sim)
    o.write("{}\n".format("\t".join(sim_lst))) 
o.close()

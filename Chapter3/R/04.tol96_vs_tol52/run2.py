#!/usr/bin/env python

import natsort
from numpy import dot
from numpy.linalg import norm
from collections import defaultdict

counter = 0 
tol_sbs52_sig_hsh = defaultdict(list)
for line in open("dtol_sbs52_sigs.tsv").readlines()[1:]:
    arr = line.strip().split("\t")
    for i, j in enumerate(arr):
        if i == 0:
            continue
        tol_sbs52_sig_hsh[i].append(float(j))

tol_sbs96_sig_hsh = defaultdict(list)
for line in open("dtol_sbs96_to_sbs52_sigs.tsv").readlines()[1:]:
    arr = line.strip().split("\t")
    for i, j in enumerate(arr):
        if i == 0:
            continue
        tol_sbs96_sig_hsh[i].append(float(j))


o = open("tol96_in_sbs52_vs_tol52.tsv", "w")
tol_sbs52_sig_lst = natsort.natsorted([str("TOL{}".format(i)) for i in list(tol_sbs52_sig_hsh.keys())])
o.write("{}\n".format("\t".join(tol_sbs52_sig_lst)))
for i, ip in tol_sbs96_sig_hsh.items():
    sim_lst = [str("TOL{}".format(i))]
    for j, jp in tol_sbs52_sig_hsh.items():
        sim = str(dot(ip, jp)/(norm(ip)*norm(jp)))
        sim_lst.append(sim)
    o.write("{}\n".format("\t".join(sim_lst))) 
o.close()

import sys
import natsort
import argparse
import itertools


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="file to read HDP csv"
    )
    args = args[1:]
    return parser.parse_args(args)


    
def csv2tsv(infile):

    sbs96_lst = []
    e = int(open(infile).readline().strip().split(",")[-1])
    hsh = {i: [] for i in range(1, e+1)}
    for line in open(infile).readlines()[1:]:
        arr = line.strip().split(",")
        sub = arr[0]
        tri = arr[1]
        sbs96 = "{},{}".format(sub, tri)
        sbs96_lst.append(sbs96)
        for j, k in enumerate(arr[2:], 1):
            hsh[j].append(float(k))

    for x in hsh:
        o = open("SBS{}.tsv".format(x), "w")
        o.write("sub\ttri\tsbs96\tcounts\tnormcounts\n")
        for y, z in enumerate(hsh[x]):
            sbs96 = sbs96_lst[y]
            ref, _, alt, _, upstream, _, downstream = list(sbs96)
            sub = "{}>{}".format(ref, alt)
            tri = "{}{}{}".format(upstream, ref, downstream)
            o.write("{}\t{}\t{}\t{}\t{}\n".format(sub, tri, sbs96, ".", z))
        o.close()

def main():
    options = parse_args(sys.argv)
    csv2tsv(options.input)
    sys.exit(0)


if __name__ == "__main__":
    main()


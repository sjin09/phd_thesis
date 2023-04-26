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
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="file to read HDP csv"
    )
    args = args[1:]
    return parser.parse_args(args)


    
def csv2attribution(infile, outfile):

    hsh = {}
    sample_lst = []
    e = int(open(infile).readline().strip().split(",")[-1])
    for line in open(infile).readlines()[1:]:
        arr = line.strip().split(",")
        sample = arr[0]
        hsh[sample] = arr[1:]
        sample_lst.append(sample)

    o = open(outfile, "w")
    o.write("sample\tmutsig\tattribution\n")
    for sample in sample_lst:
        for i, j in enumerate(hsh[sample]):
            o.write("{}\tSBS{}\t{}\n".format(sample, i, float(j)))
    o.close()


def main():
    options = parse_args(sys.argv)
    csv2attribution(options.input, options.output)
    sys.exit(0)


if __name__ == "__main__":
    main()


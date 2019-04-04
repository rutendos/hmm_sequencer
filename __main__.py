import argparse
import main

parser = argparse.ArgumentParser(description = 'Generating sequences using a first order HMM')

parser.add_argument('-f', '--frequencies', dest="freq", help = 'per position base frequency', metavar="FILE")
parser.add_argument('-e', '--experiment', dest="exp", help = 'title of experiment ie. author_year', metavar="STR")
parser.add_argument('-o', '--outdirectory', dest="outdir", help = 'directory for output', metavar="DIR")
parser.add_argument('-l', '--sequence_len', dest="len",type=int, default=3001 ,help = 'sequence length', metavar="INT")
parser.add_argument('-n', '--sequence_num', dest="num",type=int, default=500, help = 'number of sequences to be generated', metavar="INT")

args = parser.parse_args()

main.run(args.freq, args.exp, args.outdir, args.len, args.num)

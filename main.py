#----------------------------------------
# Outside imports
#----------------------------------------

import numpy as np

#----------------------------------------
# Local imports
#----------------------------------------
from sequence_generator import sequence_input 
from sequence_generator import sequence_generator 
from sequence_generator import write_fasta

np.random.seed(42)

def run(tfea_csv, experiment, outdir, seq_len = 3001, N=500):

    print("Per-base sequence frequency")
    ##get the sequences from teh frequency calculator
    sequences = sequence_input(tfea_csv)

    print("Generating sequences")
    ##generate sequences
    sequences_generating = sequence_generator(sequences, experiment, seq_len=seq_len, N = N)

    print("writing sequences to fasta file")
    ##write sequences to fasta file
    write_fasta(sequences_generating, experiment, outdir)
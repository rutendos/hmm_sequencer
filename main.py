#----------------------------------------
# Outside imports
#----------------------------------------

import sys
import time
import numpy as np

#----------------------------------------
# Local imports
#----------------------------------------
from sequence_generator import sequence_input 
from sequence_generator import sequence_generator 
from sequence_generator import write_fasta

##original seed was 42 (for the Allen et al. 2014 data)
#np.random.seed(42)


def global_seed():

    print("-----------Setting seed for the sequence generator.-----------")

    ##TO CONSIDER : time.time_ns()? this will return time in nano seconds as an integer 
    ##ALSO CONSIDER: time.monotonis
    print("time in fractional seconds of ...................:", time.time())
    print("time as an interger                              :",int(time.time()))
    print("setting seed on the clock                        : ")
    ##np.random.seed(int(time.monotonic()))
    return(int(time.time()))
    print("generating sequences.............................: ")

    print("np.random.random(",int(time.time()),") => ",np.random.random())

def run(tfea_csv, experiment, outdir, N=500, seed=True):
    
    logfile=''.join([outdir, '/', experiment, '_LOG.txt'])
    sys.stdout = open(logfile, "w")
    print ("Log file for sequences generated based on some back ground distribution. \n")

    if seed == 0:
        np.random.seed()
        print("--------------------------------------------------------------")
        print("-----------Setting seed for the sequence generator.-----------")
        print("Using random seed..............................")
        print("WARNING: Sequences generated using a random seed can not be reproduced.")
    elif seed is True:
        np.random.seed(global_seed())
    else:
        np.random.seed(seed)
        print("--------------------------------------------------------------")
        print("-----------Setting seed for the sequence generator.-----------")
        print("User defined seed..............................:", seed, "\n")

    print("--------------------------------------------------------------")
    print("-----------Reading per-base sequence frequency----------------", "\n")
    ##get the sequences from teh frequency calculator
    position_prob = sequence_input(tfea_csv)

    print("--------------------------------------------------------------")
    print("-----------Generating sequences-------------------------------", "\n")
    ##generate sequences
    #sequences_generating = sequence_generator(sequences, experiment, seq_len=seq_len, N = N)
    generating_sequences = new_sequence_generator(bases=['A', 'T', 'G', 'C'], N=N, position_feq=position_prob)

    generating_headers = fasta_header(experiment, N = N)

    print("--------------------------------------------------------------")
    print("-----------Writing sequences to fasta file--------------------", "\n")
    ##write sequences to fasta file
    #write_fasta(sequences_generating, experiment, outdir)
    write_fasta(generating_sequences, generating_headers, experiment, outdir)

    print("--------------------------------------------------------------")
    print("----------------------------DONE------------------------------")
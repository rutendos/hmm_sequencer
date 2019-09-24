#--------------------------------------
#Extenal imports
#--------------------------------------

import numpy as np


def sequence_input(sequence):
    '''takes in sequences from base_content that are in .csv format and 
    frequencies per position to use in simulating sequences using a 
    1st order Markov Model.

    Parameters
    ----------
    sequence : csv file 
        with columns of sequences (A, T, G, C)
    
    Returns
    -------
    position_frequencies : list of lists
        per position base frequencies 
        a list for each position

    
    '''

    position_feq = []

    with open(sequence) as seq:

        ##remove the header line
        lines = seq.readlines()[1:]
        for i in range(len(lines)):
            pos_prob = []
            try:
                pos_prob.append(lines[i].strip('\n').split(',')[1])
                pos_prob.append(lines[i].strip('\n').split(',')[2])
                pos_prob.append(lines[i].strip('\n').split(',')[3])
                pos_prob.append(lines[i].strip('\n').split(',')[4])
                position_feq.append(pos_prob)
            except IndexError:
                
                pos_prob.append(lines[i].strip('\n').split('\t')[1])
                pos_prob.append(lines[i].strip('\n').split('\t')[2])
                pos_prob.append(lines[i].strip('\n').split('\t')[3])
                pos_prob.append(lines[i].strip('\n').split('\t')[4])
                position_feq.append(pos_prob)
            else:
                print("Check the input file. \n It should be tab or comma separated")


    return(position_feq)
        
def sequence_generator(bases,position_feq, N=500):
    '''takes in frequencies per position and simulates sequences using a 
    1st order Markov Model.

    Parameters
    ----------
    bases : list
        list of bases to draw from

    position_feq : list of lists 
        per position base frequencies

    N : int
        number of sequences to be generated
    
    Returns
    -------
    generated_seqs : list
        list of sequences generated

    '''

    sequences = np.empty([N, len(position_feq)], dtype=str)
    
    for i in range(len(position_feq)):
        column = np.random.choice(bases, N, p=position_feq[i])
        sequences[:,i] = column
        
    joined_sequences = [''.join(row) for row in sequences]
    
    return joined_sequences

def fasta_header(exp, N):
    """Generates random headers for the fasta file
    
    Parameters
    ----------
    exp : str
        name of experiment (no spaces)
    N : int
        number of headers to be generated
    
    Returns
    -------
    headers : list
        names for each sequence (arbritrary)
    """
    
    headers =  [''.join(['>',exp,'_random_sequence_',str(i)]) for i,
                x in enumerate(list(range(int(N))))]
    
    return headers


def write_fasta(generated_sequences, headers, exp, outdir):
    ''' writes sequences generated into fasta format
    '''

    out_file = open(outdir + str(exp) + "_simulated.fa", "w")

    for i in range(len(generated_sequences)):
        out_file.write(str(headers[i]) + "\n" + str(generated_sequences[i]) + "\n" )
    out_file.close()

# hmm_sequencer
A script to generate genomic sequences from a background distribution.

## Requirements 
- python3
- argparse
- numpy 
- sys
- time

# Usage

## Help command
For general usage, used the help command

```sh
$ python3 /bin/hmm_sequencer -h

```

usage: hmm_sequencer [-h] [-f FILE] [-e STR] [-o DIR] [-l INT] [-n INT]
                     [-s INT]

Generating sequences using a first order HMM

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --frequencies FILE
                        per position base frequency
  -e STR, --experiment STR
                        title of experiment ie. author_year
  -o DIR, --outdirectory DIR
                        directory for output
  -l INT, --sequence_len INT
                        sequence length
  -n INT, --sequence_num INT
                        number of sequences to be generated
  -s INT, --seed INT    seed for initializing the random number generator. To
                        set a specific seed -s INT. The dafault is "True" so
                        the seed is based on the clock. If "0" a random seed
                        will be selected.

## Running command


```sh
python3 /path/to/hmm_sequencer -f base_content.tsv -o outdirectory/ -l 3001 -n 5000 -e Allen2014_seedOnTime

```

### Input

The command below takes in a .tsv file with each row containing per base sequence composition (below is an example of the first 5 and last 5 positions). The base composition shown below is an average across a eRNAs called by Tfit and composition summarized by "base_content" (https://github.com/rutendos/base_content). 

	A	T	G	C
0	0.27946011420661016	0.26613600969025786	0.23118186537463228	0.22322201072849973
1	0.27703754974909156	0.26578992905346943	0.22945146219069043	0.22772105900674858
2	0.2836130818480706	0.26613600969025786	0.23152794601142065	0.2187229624502509
3	0.2763453884755148	0.26803945319259387	0.23239314760339158	0.22322201072849973
4	0.2761723481571206	0.2701159370133241	0.23671915556324624	0.21699255926630906

.
.
.

2996	0.270505277729711	0.27517736632635403	0.22620695622079945	0.2281103997231355
2997	0.2634106246755494	0.27137047932168196	0.23589721405087385	0.22932168195189478
2998	0.27396608409759476	0.2795033742862087	0.2218809482609448	0.22464959335525178
2999	0.26981311645613426	0.2769077695102959	0.22603391590240526	0.22724519813116456
3000	0.26237238276518426	0.2840024225644575	0.22222702889773316	0.231398165772625


### Output

A fasta file with the number of sequences specified (5000 in the example) and the width of the sequences (3001 in the example). In addition, for reproducibility purposes, a log file containing the seed used for the run will also be exported.  

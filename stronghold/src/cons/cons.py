"""
    http://rosalind.info/problems/cons/

    Given:  A collection of at most 10 DNA strings of equal length 
            (at most 1 kbp) in FASTA format.

    Return: A consensus string and profile matrix for the collection. 
            (If several possible consensus strings exist, 
            then you may return any one of them.)
"""
import re
from pprint import pprint


PAD = "*"
FASTA_HEADERS = re.compile(">(.+)")
FASTA_DNA_SEQ = re.compile("^([ACGT\n]+)")

def parse_fasta(string):
    """
    Accepts a FASTA string and returns a dictionary (header -> sequence)
    """
    lines = string.split('\n')
    headers = []
    sequences = []
    for line in lines:
        is_header = FASTA_HEADERS.match(line)
        is_sequence = FASTA_DNA_SEQ.match(line)
        if is_header:
            headers.append(is_header.group())
            sequences.append('*')
        elif is_sequence:
            sequences.append(is_sequence.group())
    
    # The first step here creates a blank list element at the head of list
    # so zip only works with n - 1 elems and a blank. So we filter list
    sequences = ''.join(sequences).split('*')
    sequences = [s for s in sequences if s]
    return dict(zip(headers, sequences))

def normalize(dnas):
    """
    Pad strings in list with * to make sure all of them have the same length
    """
    len_max = max([len(s) for s in dnas])
    return [s + (PAD * (len_max - len(s))) for s in dnas]

def make_profile(dnas):
    """
    Returns a profile matrix using all elements of dnas
    """
    profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    dnas = normalize(dnas)
    dna_matrix = [[base for base in strand] for strand in dnas]
    
    # Fine to go with first since they all have the same length now
    length = len(dna_matrix[0])
    
    for i in xrange(0, length):
        m = [dna[i] for dna in dna_matrix]

        for k in profile_matrix.keys():
            profile_matrix[k].append(m.count(k))
    
    return profile_matrix

def consensus(profile_matrix):
    """
    Spaghetti function
    Returns the consensus strand give the DNA profile matrix
    """
    sorted_keys = sorted(profile_matrix.keys())
    profile = []
    cons = []
    for k in sorted_keys:
        profile.append([(k, v) for v in profile_matrix[k]])
    portrait = zip(*profile)
    for row in portrait:
        labels, counts = zip(*row)
        cons.append(labels[counts.index(max(counts))])
    return ''.join(cons)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Usage: python %s <filename>" % sys.argv[0]
    else:
        fname = sys.argv[1]
        data = open(fname).read()
        strands = parse_fasta(data).values()
        profile = make_profile(strands)
        cons = consensus(profile)
        print cons
        sorted_profile_matrix = sorted(profile.iteritems())
        for k, v in sorted_profile_matrix:
            print "%s: %s" % (k, ' '.join(str(u) for u in v))

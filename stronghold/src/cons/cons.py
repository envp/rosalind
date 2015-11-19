"""
    http://rosalind.info/problems/cons/

    Given:  A collection of at most 10 DNA strings of equal length 
            (at most 1 kbp) in FASTA format.

    Return: A consensus string and profile matrix for the collection. 
            (If several possible consensus strings exist, 
            then you may return any one of them.)
"""
import re


PAD = "*"
FASTA_HEADERS = re.compile(">(.+)")
FASTA_DNA_SEQ = re.compile("([ACGT\n]+)")

def parse_fasta(string):
    """
    Accepts a FASTA string and returns a dictionary (header -> sequence)
    """
    headers = FASTA_HEADERS.findall(string)
    sequences = map(lambda s: s.replace('\n', ''), 
                    FASTA_DNA_SEQ.findall(string))
    return dict(zip(headers, sequences))

def normalize(dnas):
    """
        Pad strings in list with * to make 
        sure all of them have the same length
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
    pass
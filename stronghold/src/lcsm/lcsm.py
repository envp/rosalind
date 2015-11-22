"""
    Find the longest common substring of two DNA strands

    Given:  A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

    Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
import re
import itertools


FASTA_HEADERS = re.compile(">(.+)")
FASTA_DNA_SEQ = re.compile("([ACGT\n]+)")


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
            headers.append(is_header.group().strip()[1:])
            sequences.append('*')
        elif is_sequence:
            sequences.append(is_sequence.group())
    
    # The first step here creates a blank element at the head of list
    # so zip only works with n - 1 elems and a blank. So we filter list
    sequences = ''.join(sequences).split('*')
    sequences = [s for s in sequences if s]
    return dict(zip(headers, sequences))


def lcs(s1, s2):
    
if 
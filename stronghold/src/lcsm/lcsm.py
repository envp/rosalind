# -*- coding: utf-8 -*-
"""
    Find the longest common substring of two DNA strands

    Given:  A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

    Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
import re
import sys

from itertools import izip
from functools import reduce


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
    """
    http://en.wikipedia.org/wiki/Longest_common_substring_problem#Pseudocode
    """
    L = {}
    z = 0
    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                L[(i, j)] = L.get((i - 1, j - 1), 0) + 1
                if L[(i, j)] > z:
                    z = L[(i, j)]
                    ret = s1[i - z + 1:i + 1]
    return ret
    


def longest_common_substring(*strings):
    # LCS(A, B, C, D) = LCS(LCS(A, B), C) or any other permutation
    # Returns 'a LCS', may not even be the same as the example
    return reduce(lcs, strings)

if __name__ == "__main__":
    import sys
    fname = sys.argv[1]
    data = open(fname).read()
    parsed_data = parse_fasta(data)
    data_iterator = parsed_data.itervalues()
    lcs = longest_common_substring(*data_iterator)
    print lcs
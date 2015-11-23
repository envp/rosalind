# -*- coding: utf-8 -*-
"""
    Find the longest common substring of two DNA strands

    Given:  A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

    Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
import re
from itertools import izip
import sys


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

def suffixes(s):
    """
    Returns sorted suffix list of a string
    """
    length = len(s)
    suffix_list = [(i, s[i:]) for i in xrange(length)]
    
    # Sort by suffix
    return sorted(suffix_list, key=lambda a: a[1])

def lc_prefix(suffix_list):
    """
    Returns the LCP array given a suffix array
    """
    suf_array = zip(*suffix_list)[1]
    lcp = [-1]
    length = len(suf_array)
    for i in xrange(1, length):
        s = suf_array[i - 1]
        t = suf_array[i]
        #print "### %s, %s" % (s, t)
        #print "##", [a == b for a, b in izip(s, t)]
        prefix_length = sum([a == b for a, b in izip(s, t)])
        lcp.append(prefix_length)
    return lcp

def lcs(s1, s2):
    s = '$'.join([s1, s2])
    suffix_array = suffixes(s)
    lcp = lc_prefix(suffix_array)
    z = zip(*suffix_array)[1]
    print z
    print lcp
    print z[lcp.index(max(lcp))], z[lcp.index(max(lcp)) + 1]

lcs(sys.argv[1], sys.argv[2])
"""
    http://rosalind.info/problems/grph/
    
    Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

    Return: The adjacency list corresponding to O3. You may return edges in any order.
"""
import re


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
    
    # The first step here creates a blank list element at the head of list
    # so zip only works with n - 1 elems and a blank. So we filter list
    sequences = ''.join(sequences).split('*')
    sequences = [s for s in sequences if s]
    return dict(zip(headers, sequences))

def adjecency_list(dnas, k=3):
    """
    Returns the adjacency list for length k suffix matching a k-long prefix
    Defaults to computing for k=3
    """
    adj = []
    for h1, d1 in dnas.iteritems():
        for h2, d2 in dnas.iteritems():
            if (d1 is not d2) and (d1[-k:] == d2[:k]):
                adj.append((h1, h2))
    return adj

def grph(data):
    dnas = parse_fasta(data)
    return adjecency_list(dnas)
    
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print "Usage: python %s <filename>" % sys.argv[1]
    else:
        fname = sys.argv[1]
        data = open(fname).read()
        adj = grph(data)
        for row in adj:
            print ' '.join(row)
"""
    http://rosalind.info/problems/dna/
    
    Count the number of different in a given DNA string

    Given: A DNA string s of length at most 1000 nt.

    Return: Four integers (separated by spaces) counting 
            the respective number of times that the symbols 
            'A', 'C', 'G', and 'T' occur in s.
"""

NUCLEOTIDES = ['a', 'c', 'g', 't']

def count_nucleotides(string):
    string = string.lower()
    base_count = {x: string.count(x) for x in NUCLEOTIDES}
    return base_count


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Usage: python %s <STRING>" % sys.argv[0]
    else:
        dna = sys.argv[1]
        base_count = count_nucleotides(dna)
        stringified_count = [str(base_count[k]) for k in NUCLEOTIDES]
        print ' '.join(stringified_count)

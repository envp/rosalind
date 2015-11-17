"""
    http://rosalind.info/problems/revc/
    
    Compute the reverse complement of a DNA string

    Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement sc of s.
"""

NUCLEOTIDES = ['a', 'c', 'g', 't']

COMPLEMENT_MAP = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}

def reverse_complement(string):
    is_lower = string.islower()
    is_upper = string.isupper()
    string = string.lower()
    revc = ''.join([COMPLEMENT_MAP[s] for s in reversed(string)])
    
    if is_upper and not is_lower:
        # Originally uppercase
        return revc.upper()
    else:
        # Originally lowercase / mixed case
        return revc.lower()
        
        
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Usage: python %s <STRING>" % sys.argv[0]
    else:
        dna = sys.argv[1]
        print reverse_complement(dna)

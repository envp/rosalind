"""
    Transcribe a DNA string to a RNA string

    Given: A DNA string t having length at most 1000 nt.

    Return: The transcribed RNA string of t.
"""

NUCLEOTIDES = ['a', 'c', 'g', 't']

COMPLEMENT_MAP = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}


def to_rna(string):
    is_upper = string.isupper()
    is_lower = string.islower()
    string = string.lower()
    string = string.replace('t', 'u')
    
    if is_upper and not is_lower:
        # Originally uppercase
        return string.upper()
    else:
        # Originally lowercase / mixed case
        return string.lower()

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Usage: python %s <STRING>" % sys.argv[0]
    else:
        dna = sys.argv[1]
        transcribed = to_rna(dna)
        print transcribed.upper()

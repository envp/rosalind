class DNA(object):
    """
        Compute the reverse complement of a DNA string

        Given: A DNA string s of length at most 1000 bp.

        Return: The reverse complement sc of s.
    """

    NUCLEOTIDES = ['a', 'c', 'g', 't']

    COMPLEMENT_MAP = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}

    def __init__(self, string):
        self.string = string.lower()

    def reverse_complement(self):
        if self.COMPLEMENT_MAP:
            rev = [self.COMPLEMENT_MAP[s] for s in reversed(self.string)]
            return ''.join(rev)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Usage: python %s <STRING>" % sys.argv[0]
    else:
        string = sys.argv[1]
        dna = DNA(string)
        print dna.reverse_complement().upper()

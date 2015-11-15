class DNA(object):
    """
        Count the number of different in a given DNA string

        Given: A DNA string s of length at most 1000 nt.

        Return: Four integers (separated by spaces) counting 
                the respective number of times that the symbols 
                'A', 'C', 'G', and 'T' occur in s.
    """

    NUCLEOTIDES = ['a', 'c', 'g', 't']

    def __init__(self, string):
        self.string = string.lower()

    def count_nucleotides(self):
        base_count = {x: self.string.count(x) for x in self.NUCLEOTIDES}
        return base_count


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Usage: python %s <STRING>" % sys.argv[0]
    else:
        string = sys.argv[1]
        dna = DNA(string)
        base_count = dna.count_nucleotides()
        strigified_count = [str(base_count[k]) for k in dna.NUCLEOTIDES]
        print ' '.join(strigified_count)

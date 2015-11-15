class DNA(object):
    """
        Transcribe a DNA string to a RNA string

        Given: A DNA string t having length at most 1000 nt.

        Return: The transcribed RNA string of t.
    """

    NUCLEOTIDES = ['a', 'c', 'g', 't']

    COMPLEMENT_MAP = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}

    def __init__(self, string):
        self.string = string.lower()

    def to_rna(self):
        return self.string.replace('t', 'u')


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Usage: python %s <STRING>" % sys.argv[0]
    else:
        string = sys.argv[1]
        dna = DNA(string)
        transcribed = dna.to_rna()
        print transcribed.upper()

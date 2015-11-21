"""
    http://rosalind.info/problems/iev/

    Given:  Six positive integers, each of which does not exceed 20,000.
            The integers correspond to the number of couples in a population
            possessing each genotype pairing for a given factor.
            In order, the six given integers represent the
            number of couples having the following genotypes:
            1. AA-AA
            2. AA-Aa
            3. AA-aa
            4. Aa-Aa
            5. Aa-aa
            6. aa-aa

    Return: The expected number of offspring displaying the dominant phenotype
            in the next generation, under the assumption that
            every couple has exactly two offspring.
"""


from operator import mul as OP_MUL
from itertools import imap


# For each of the each given combinations
# Keep an LUT that stores the probability of having dom phenotype in offspring
DOM_OFFSPRING_TABLE = [1, 1, 1, 0.75, 0.5, 0]


def iev(population, num_offspring=2):
    assert len(population) == 6
    # Each type of population has the same number of offsprings in next gen
    offsprings = imap(lambda p: num_offspring * p, population)
    return sum(imap(OP_MUL, DOM_OFFSPRING_TABLE, offsprings))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 7:
        print "Usage: python %s <number of members of each population: n1, n2, n3, n4, n5, n6>"
    else:
        data = map(int, sys.argv[1:])
        print iev(data)

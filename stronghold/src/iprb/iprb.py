"""
    http://rosalind.info/problems/iprb/
    
    Given the populations of various genotypes, determine the probability of a 
    specific phenotype emerging in the next generation
    
    Given:  Three positive integers k, m, and n, representing a population 
            containing k+m+n organisms: 
            k individuals are homozygous dominant for a factor, 
            m are heterozygous, and 
            n are homozygous recessive.

    Return: The probability that two randomly selected mating organisms will 
            produce an individual possessing a dominant allele 
            (and thus displaying the dominant phenotype). 
            Assume that any two organisms can mate.
"""
from __future__ import division


def comb(n, r):
    """
    Return binomial coefficients C(n, r)
    """
    if r == 1:
        return n
    else:
        return (n / r) * comb(n - 1, r - 1)

def iprb(k, m, n):
    """
    This can only be explained via punnett squares:

    There are 5 pairings that lead to a dominant phenotype (ignoring ordering):
    (XX,XX), (XX,Xx), (XX,xx), (Xx,Xx), (Xx, xx)
    Each of these pairs produce 4, 4, 4, 3 and 2 dominant phenotypes respectively:

     |X |X |**|X |x |**|x |x |
     +--+--+--+--+--+--+--+--+
    X|XX|XX|**|XX|Xx|**|Xx|Xx|
     +--+--+--+--+--+--+--+--+
    X|XX|XX|**|XX|Xx|**|Xx|Xx|
     +--+--+--+--+--+--+--+--+
              |X |x |
              +--+--+
             x|Xx|xx|
              +--+--+             
             x|Xx|xx|
              +--+--+
              |X |x |
              +--+--+
             X|XX|Xx|
              +--+--+
             x|Xx|xx|
    """
    total_matings = 4 * (k*m + k*n + n*m +comb(k, 2) + comb(n, 2) + comb(m, 2))
    dominant = 4 * (comb(k, 2) + k*m + k*n) + 3 * comb(m, 2) + 2*m*n
    
    return dominant / total_matings
    

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print "Usage: python %s <k> <m> <n>" % sys.argv[0]
    else:
        k, m, n = map(int, sys.argv[1:4])
        print iprb(k, m, n)

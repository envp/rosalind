# -*- coding: utf-8 -*-

"""
    http://rosalind.info/problems/fib/
    
    Count the number of rabbit pairs in the nth generation given k pairs

    Given: Positive integers n≤40 and k≤5.
        
    Return: The total number of rabbit pairs that will be present after
            n months if each pair of reproduction-age rabbits produces 
            a litter of k rabbit pairs in each generation 
            (instead of only 1 pair).
"""

def rabbits(n, k):
    fs = [1, 1]
    for i in xrange(0, n-2):
        # Evaluate n - 2 terms as first two are already known
        fs.append(fs[-1] + k * fs[-2])
    return fs[-1]

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print "Usage: python %s <n> <k>" % sys.argv[0]
    else:
        n, k = int(sys.argv[1]), int(sys.argv[2])
        print rabbits(n, k)
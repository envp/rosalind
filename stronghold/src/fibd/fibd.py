# -*- coding: utf8 -*-
"""
    http://rosalind.info/problems/fibd/
    
    Find the nth term in a fibonacci sequence as if it were for mortal rabbits
    that survived m-iterations on average
    
    Given:  Positive integers n≤100 and m≤20.

    Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""
from collections import deque


def rabbits(n, m):
    rs = deque([0] * (m - 2) + [1, 1, 1])

    if n < 2:
        return 1
    if m < 2:
        return 0

    for i in xrange(2, n):
        rs.append(rs[-1] + rs[-2] - rs[-m-1])
        rs.popleft()

    return rs[-1]


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print "Usage: python %s <n> <m>" % sys.argv[0]
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        r = rabbits(n, m)
        print r
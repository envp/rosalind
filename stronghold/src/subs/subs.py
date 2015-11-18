"""
    http://rosalind.info/problems/subs/
    
    Given two strings s and t, t is a substring of s if t is contained as a
    contiguous collection of symbols in s 
    (as a result, t must be no longer than s).
    
    Given:  Two DNA strings s and t (each of length at most 1 kbp).

    Return: All locations of t as a substring of s.
"""

import re

def motif(s, t):
    # This boils down to finding overlapping regex matches of the substring
    return [p.start() + 1 for p in re.finditer(r'(?=(%s))' % t, s)]
    
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print "Usage python %s <filename>" % sys.argv[0]
    else:
        fname = sys.argv[1]
        data = open(fname).read()
        
        # Damn this windows line ending
        s, t = data.split('\r\n')[:2]
        print ' '.join(map(str, motif(s, t)))

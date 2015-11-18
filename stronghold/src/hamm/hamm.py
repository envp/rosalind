"""
    http://rosalind.info/problems/hamm/
    
    Compute the hamming distance between two strands of DNA (equal length)
    
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp)

    Return: The Hamming distance d(s,t)
"""

def hamming(s1, s2):
    """
    Returns the hamming distance between two strings s1 and s2
    """
    l1 = list(s1)
    l2 = list(s2)
    return [p != q for p, q in zip(l1, l2)].count(True)
    
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print "Usage: python %s <filename>" % sys.argv[0]
    else:
        fname = sys.argv[1]
        s1, s2 = open(fname).read().split('\n')[0:2]
        print hamming(s1, s2)

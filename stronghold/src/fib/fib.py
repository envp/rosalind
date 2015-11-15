class GeneralizedFibonacci(object):
    """ 
        Model a generalized fibonacci sequence:
        F(n) = a(0) + SUM(a(t)*F(n-t), 1, k)
        
        Where,
        * a(t): Sequence coefficients
        * k: Fan width or divergence of the recurrent sequence
        
        Given: Positive integers n ≤ 40 and k ≤ 5.

        Return: The total number of rabbit pairs that will be present after
                n months if we begin with 1 pair and in each generation, 
                every pair of reproduction-age rabbits produces a litter of 
                k rabbit pairs (instead of only 1 pair).
    """
    
    def __init__(self, width, coeffts):
        try:
            assert width == len(coeffts)
            self.coefft = coeffts
            self.width =
            
        except AssertionError, e:
            print "Number of coefficients should match recurrence tree width"
            print e.args

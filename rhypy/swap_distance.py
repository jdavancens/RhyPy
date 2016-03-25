# -*- coding: utf-8 -*-

def swap_distance(self, A, B):
    r''' A special instance of the "earth mover's distance," which measures
    the dissimilarity of two equal length rhythms. Basically, the sum of the
    absolute values of the differences between the elements of A and B.
    '''
    from rhypy import Rhythm
    assert isinstance(A, Rhythm) and isinstance(B, Rhythm) , \
        "Both parameters must be of type Rhythm"

    assert len(A) == len(B) , "Rhythms must be the same length"
    return sum([abs(a-b) for a,b in zip(A,B)])

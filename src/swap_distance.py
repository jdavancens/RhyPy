# -*- coding: utf-8 -*-
def swap_distance(self, A, B):
    r''' A special instance of the "earth mover's distance," which measures
    the dissimilarity of two equal length rhythms.
    '''
    from rhypy import Rhythm
    assert(isinstance(A, Rhythm) and isinstance(B, Rhythm))
    assert(len(A) == len(B))
    return sum([abs(a-b) for a,b in zip(A,B)])

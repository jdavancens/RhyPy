# -*- coding: utf-8 -*-
from rhypy import Rhythm
import math

''' Drawn from Toussaint, "A Comparison of Rhythmic Dissimilarity Measures"
Forma, 21, 129-149, 2006.
'''

def chronotonic(A, B):
    ''' Chronitonic distance: the difference of the sum of squares of inter-onset
    interval vectors A and Bs

    .. container:: example

        **Example 1.** Gets hamming distance of two Rhythms:

        ::
            >> rhythm_a = Rhythm([1,0,1,0])
            >> rhythm_b = Rhythm([1,1,0,0])
            >> distance.chronotonic(rhythm_a, rhythm b)

    '''
    assert isinstance(A, Rhythm) and isinstance(B, Rhythm) , \
        "Both parameters must be of type Rhythm"
    assert len(A) == len(B) , "Rhythms must be the same length"
    Ai = A.inter_onset_intervals
    Bi = B.inter_onset_intervals
    return abs(sum([x*x for x in A]) - sum([x*x for x in B]))

def euclidian(A, B):
    ''' Euclidian interval vector distance: the square root of the sum of the
    squared differences between the elements of A and B.

    .. container:: example

        **Example 1.** Gets hamming distance of two Rhythms:

        ::
            >> rhythm_a = Rhythm([1,0,1,0])
            >> rhythm_b = Rhythm([1,1,0,0])
            >> distance.euclidian(rhythm_a, rhythm b)

    '''
    assert isinstance(A, Rhythm) and isinstance(B, Rhythm) , \
        "Both parameters must be of type Rhythm"
    assert len(A) == len(B) , "Rhythms must be the same length"
    Ai = A.inter_onset_intervals
    Bi = B.inter_onset_intervals
    return math.sqrt(sum((a-b)**2 for a,b in zip(Ai,Bi)))

def hamming(A, B):
    ''' Hamming distance: the sum of the absolute values of the differences
    between the elements of binary strings A and B.

    .. container:: example

        **Example 1.** Gets hamming distance of two Rhythms:

        ::
            >> rhythm_a = Rhythm([1,0,1,0])
            >> rhythm_b = Rhythm([1,1,0,0])
            >> distance.hamming(rhythm_a, rhythm b)

    '''

    assert isinstance(A, Rhythm) and isinstance(B, Rhythm) , \
        "Both parameters must be of type Rhythm"
    assert len(A) == len(B) , "Rhythms must be the same length"
    return sum([abs(a-b) for a,b in zip(A,B)])


#TODO: def interval_difference_vector(A, B)

def swap(A, B):
    ''' Swap distance: the sum of the absolute values of the differences
    between the elements of onset vectors A and B.

    .. container:: example

        **Example 1.** Gets hamming distance of two Rhythms:

        ::
            >> rhythm_a = Rhythm([1,0,1,0])
            >> rhythm_b = Rhythm([1,1,0,0])
            >> distance.swap(rhythm_a, rhythm b)

    '''

    assert isinstance(A, Rhythm) and isinstance(B, Rhythm) , \
        "Both parameters must be of type Rhythm"
    assert len(A) == len(B) , "Rhythms must be the same length"
    Ao = A.onsets
    Bo = B.onsets
    return sum([abs(a-b) for a,b in zip(Ao,Bo)])

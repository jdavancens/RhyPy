# -*- coding: utf-8 -*-
import math
class Rhythm(object):
    ''' A musical rhythm represented as an onset vector: a binary event list of
    onsets and rests.

    '''

    __slots__ = ('_event_list',)

    ### INITIALIZER ###

    def __init__(self, event_list):
        self._event_list = [bool(x) for x in event_list]

    ### SPECIAL METHODS ###

    def __getitem__(self, i):
        r'''Gets item at index.

            ::

                >>> rhythm = Rhythm([1,0,1])
                >>> rhythm[2]
                1

        Returns boolean.
        '''
        k = len(self._event_list)
        i = i % k
        return self._event_list[i]

    def __len__(self):
        r'''Gets the length of the rhythm.

            ::

                >>> rhythm = Rhythm([1,0,1])
                >>> len(rhythm)
                3

        Returns integer
        '''
        return len(self._event_list)

    def __repr__(self):
        r'''Gets string representation of rhythm in musicological TUBS format.

            ::

                >>> str(Rhythm([1,0,0,1,0,0,1,0]))
                '[x . . x . . x .]'

        Returns string.
        '''
        s = []
        for event in self._event_list:
            if event == True:
                s += 'x'
            else:
                s += '.'
        return '[' + ' '.join(s) + ']'

    ### PRIVATE METHODS ###

    def _divisors(self, n):
        n = abs(n)
        divisors = [1]
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
        codivisors = [n // i for i in reversed(divisors)]
        if divisors[-1] == codivisors[0]:
            divisors.pop()
        divisors.extend(codivisors)
        divisors.sort()
        return divisors

    ### PUBLIC METHODS ###

    def reverse(self):
        r'''Reverses the rhythm.

            ::

                >>> rhythm = Rhythm([1,1,0,0])
                >>> rhythm
                [x x . .]
                >>> rhythm.reverse()
                >>> rhythm
                [. . x x]

        '''
        self._event_list.reverse()

    def rotate(self, n):
        r'''Rotates the rhythm n places.

            ::

                >>> rhythm = Rhythm([1,1,0])
                >>> rhythm
                [x x .]
                >>> rhythm.rotate(1)
                >>> rhythm
                [x . x]

        '''
        if len(self._event_list) == 0 or self.is_empty:
            return
        k = len(self._event_list)
        n = n % k
        A = self._event_list[0:n]
        B = self._event_list[n:]
        self._event_list = B + A

    ### PUBLIC PROPERTIES ###

    @property
    def inter_onset_intervals(self):
        r''' Gets the inter-onset intervals of the rhythm.

            ::
                >>> rhythm = Rhythm([1,0,1,0,0])
                >>> rhythm.inter_onset_intervals
                [2, 3]

            ::
                >>> rhythm = Rhythm([0,1,0,1,0])
                >>> rhythm.inter_onset_intervals
                [-1, 2, 2]

        '''
        onsets = self.onsets
        intervals = []
        last = 0
        summ = 0
        for i, x in enumerate(onsets):
            interval = onsets[i] - last
            if interval != 0:
                intervals.append(interval)
            last = onsets[i]
        intervals.append(len(self._event_list) - last)
        if self[0] == 0:
            intervals[0] *= -1
        return intervals

    # @property
    # def interval_vector(self):
    #     r'''Gets the interval vector of the onset coordinates (the 'spectrum'
    #     of the rhythm)
    #
    #         ::
    #             >>> rhythm = Rhythm([1,0,1,0,1])
    #             >>> rhythm.interval_vector
    #             [0, 1, 2]
    #
    #     Returns list of integers.
    #     '''
    #     from itertools import combinations
    #     iv = [0 for i in range(len(self))]
    #     for c in combinations(self.onsets, 2): ## 0, 2, 4
    #         interval = abs(c[0]-c[1])
    #         if interval > 0:
    #             iv[interval - 1] += 1
    #     return iv

    @property
    def is_empty(self):
        for x in self._event_list:
            if x:
                return False
        return True

    @property
    def onsets(self):
        r'''Gets the onset coordinates.

            ::

                >>> rhythm = Rhythm([1,0,1,0])
                >>> rhythm.onsets
                [0, 2]

        Returns integer list of offset coordinates.
        '''
        return [i for i in range(len(self)) if self[i]]

    @property
    def ratio(self):
        r'''Gets the ratio of inter-onset intervals, including negative numbers
        for initial rests

            ::

                >>> rhythm = Rhythm([1,0,1,0,1,0])
                >>> rhythm.ratio
                [1, 1, 1]

                >>> rhythm = Rhythm([0,0,1,0,1,0])
                [1, 1, 1]

        Returns integer list of ratios.
        '''
        intervals = self.inter_onset_intervals
        all_divisors = []
        for interval in intervals:
            divisors = self._divisors(interval)
            for divisor in divisors:
                if divisor not in all_divisors:
                    all_divisors.append(divisor)
        gcd = max(all_divisors)
        ratio = [interval/gcd for interval in intervals]
        return ratio

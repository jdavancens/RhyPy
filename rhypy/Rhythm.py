# -*- coding: utf-8 -*-
class Rhythm:
    ''' A musical rhythm represented as an onset vector: a binary event list of
    onsets and rests.

    .. container:: example

        **Example 1.** Initializes from a list of integers.

        ::
            >>> Rhythm([1,0,0,1,0,0,1,0])
            [x . . x . . x .]

    .. container:: example

        **Example 2.** Initializes from a list of booleans.

        ::
            >>> Rhythm([True, False, False, True, False, False, True, False])
            [x . . x . . x .]
    '''

    __slots__ = ('_event_list',)

    def __init__(self, event_list):
        self._event_list = [bool(x) for x in event_list]

    def __len__(self):
        r'''Gets the length of the rhythm.

        .. container: example

            **Example 1.** Gets legnth

            ::

                >>> rhythm = Rhythm([1,0,1])
                >>> len(rhythm)
                3

        Returns integer
        '''
        return len(self._event_list)

    def __str__(self):
        r'''Gets string representation of rhythm in musicological TUBS format.

        .. container:: example

            **Example 1.** String representation

            ::

                >>> str(Rhythm([1,0,0,1,0,0,1,0]))
                '[x . . x . . x .]'

        Returns string.
        '''
        s = []
        for event in event_list:
            if event == True:
                s += 'x'
            else:
                s += '.'
        s = '[' + s.join(' ') + ']'
        return s.join(' ')



    def index(self, i):
        r'''Gets item at index.

        .. container:: example

            **Example 1.** Item at index:

            ::

                >>> rhythm = Rhythm([1,0,1])
                >>> rhythm.index(2)
                1

        Returns boolean.
        '''
        k = self.length
        i = i % k
        return self._event_list[i]

    def inter_onset_intervals(self):
        r''' Gets the inter-onset intervals of the rhythm.

        .. container:: example

            **Example 1.** Inter-onset intervals:

            ::
                >>> rhythm = Rhythm([1,0,1,0,0])
                >>> rhythm.inter_onset_intervals
                [2,3]

            **Example 2.** Inter-onset intervals when no downbeat:

            ::
                >>> rhythm = Rhythm([0,1,0,1,0])
                >>> rhythm.inter_onset_intervals
                [2,3]
        '''
        temp = Rhythm(self._event_list)
        # rotate until starts with onset
        while(temp[0] is 0): #TODO: account for empty rhythm -> infinite loop
            temp.rotate(1)
        intervals = []
        count = 0
        last = 0
        for i in temp._event_list:
            if i == 1:
                if count > 0:
                    intervals.append(count)
                count = 1
            else:
                count += 1
        if count > 0:
            intervals.append(count)
        return intervals



    def interval_vector(self):
        r'''Gets the interval vector of the onset coordinates (the 'spectrum'
        of the rhythm)

        .. container:: example

            **Example 1.** Interval vector:

            ::
                >>> rhythm = Rhythm([1,0,1,0,1])
                >>> rhythm.interval_vector
                [0,1,2]

        Returns list of integers.
        '''
        from itertools import combinations
        iv = [0 for i in range(self.length)]
        for c in combinations(self.onsets, 2):
            interval = abs(c[0]-c[1])
            iv[interval - 1] += 1
        return iv

    def onsets(self):
        r'''Gets the onset coordinates.

        .. container: example

            **Example 1.** Gets onsets:

            ::

                >>> rhythm = Rhythm([1,0,1,0])
                >>> rhythm.onsets
                [0,2]

        Returns integer list of offset coordinates.
        '''
        return [i for i in range(self.length) if self.index(i)]

    def reverse(self):
        r'''Reverses the rhythm.

        .. container: example

            **Example 1.** Reverses the rhythm:

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

        .. container: example

            **Example 1.** Rotates the rhythm:

            ::

                >>> rhythm = Rhythm([1,1,0])
                >>> rhythm
                [x x .]
                >>> rhythm.rotate(1)
                >>> rhythm
                [x . x]

        '''
        if len(self.event_list) == 0:
            return
        k = len(self._event_list)
        n = n % k
        A = self._event_list[0:n]
        B = self._event_list[n:]
        self._event_list = B+A

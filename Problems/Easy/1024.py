# Pair and triples

from collections import defaultdict


class Solution:
    def solve(self, s):
        mdict = defaultdict(int)
        for i in s:
            mdict[i] = (mdict[i] + 1) % 3
        two_count = 0
        other = False
        for i in mdict:
            if mdict[i] == 2:
                two_count += 1
            other = other or mdict[i] % 3 == 1
        return two_count == 1 and not other

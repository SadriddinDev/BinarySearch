class Solution: #v1 best
    def solve(self, s):
        l, r = s.count('L'), s.count('R')
        return abs(r-l) + (len(s)-l-r)


class Solution: # v2 not bad
    def solve(self, s):
        l, r, ques = 0,0,0
        for c in s:
            if c == 'L':
                l += 1
            elif c == 'R':
                r += 1
            else:
                ques += 1
        return abs(r-l) + ques
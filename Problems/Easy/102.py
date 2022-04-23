class Solution:
    def solve(self, s):
        l = ""
        c = 0
        m = 0
        for i in s:
            if i == l:
                c += 1
            else:
                l = i
                c = 1
            if c > m:
                m = c
        return m

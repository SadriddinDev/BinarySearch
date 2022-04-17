class Solution:
    def solve(self, n):
        a = 1
        b = 1
        c = a + b
        i = 1
        while i < n:
            i += 1
            a = b
            b = c
            c = a + b
        return a
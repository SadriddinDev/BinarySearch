class Solution:
    def solve(self, n):
        m = 0
        c = 0
        while n:
            if n % 2:
                c += 1
                if c > m:
                    m = c
            else:
                c = 0
            n //= 2
        return m

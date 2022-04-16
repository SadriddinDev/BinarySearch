class Solution:
    def solve(self, n):
        c = 0
        while n>0:
            c += (n%2 == 1)
            n = n // 2
        return c
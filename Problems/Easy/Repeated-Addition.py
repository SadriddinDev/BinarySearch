class Solution:
    def solve(self, n):
        while n >= 10:
            s = 0
            while n:
                s += n % 10
                n //= 10
            n = s
        return n

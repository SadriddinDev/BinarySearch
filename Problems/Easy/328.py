class Solution:
    def solve(self, n):
        m = 0
        d = 1
        b = True
        while d <= n:
            d *= 10
        while n:
            t = (n % d) // (d/10)
            if t < 3 and b:
                b = False
                m = m * 10 + 3
            else:
                m = m * 10 + t
            d = d // 10
            n = n % d
        return m

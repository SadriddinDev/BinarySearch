class Solution:
    def solve(self, n):
        if n == 0:
            return "0"
        s = ""
        while n>0:
            s = chr(48 + n%3) + s
            n = n // 3
        return s
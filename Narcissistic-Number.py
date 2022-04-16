class Solution:
    def solve(self, n):
        n1 = n
        l = len(str(n))
        s = 0
        while n:
            s += (n%10)**l
            n//=10
        return n1==s 
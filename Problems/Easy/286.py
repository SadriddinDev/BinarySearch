class Solution:
    def solve(self, a):
        n = 1
        p = 1
        while p <= a:
            if p == a:
                return n
            n+=1
            p*=n
        return -1
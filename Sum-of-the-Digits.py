class Solution:
    def solve(self, num):
        s = 0
        while num:
            s+=num%10
            num//=10
        return s
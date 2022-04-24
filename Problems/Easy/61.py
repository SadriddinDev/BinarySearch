class Solution:
    def solve(self, s):
        a = {}
        for i in range(len(s)):
            if a.get(s[i]):
                return i
            a[s[i]] = True
        return -1
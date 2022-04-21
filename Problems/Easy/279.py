class Solution:
    def solve(self, s, t):
        Hash = {}
        Hash2 = {}
        for i in range(len(s)):
            if Hash.get(s[i]):
                if Hash.get(s[i]) != t[i]:
                    return False
            else:
                if Hash2.get(t[i]):
                    return False
                Hash[s[i]] = t[i]
                Hash2[t[i]] = s[i]
        return True
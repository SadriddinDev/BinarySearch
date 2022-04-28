class Solution:
    def solve(self, s, t):
        def get_diff_count(s1, s2):
            c = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    c += 1
            return c
        tl = len(t)
        m = len(t)
        for i in range(0, len(s) - len(t)+1):
            c = get_diff_count(s[i:i+tl], t)
            if c < m:
                m = c
        return m

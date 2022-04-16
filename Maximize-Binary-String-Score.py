class Solution:
    def solve(self, s):
        one_c = s.count("1")
        zero_c = 0
        max_c = 0
        for i in range(len(s)-1):
            if s[i] == "1":
                one_c -= 1
            else:
                zero_c += 1
            max_c = max(one_c + zero_c, max_c)
        return max_c        
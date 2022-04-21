class Solution:
    def solve(self, numeral):
        s = 0
        dex_num = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
        l = len(numeral)
        for i in range(len(numeral)):
            if i < l - 1 and dex_num[numeral[i]] < dex_num[numeral[i+1]]:
                s -= dex_num[numeral[i]]
            else:
                s += dex_num[numeral[i]]
        return s

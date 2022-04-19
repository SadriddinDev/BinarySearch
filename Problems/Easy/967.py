class Solution:
    def solve(self, s):
        summ = 0
        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + ord(i) - 48
            elif num > 0:
                summ += num
                num = 0
        summ += num
        return summ
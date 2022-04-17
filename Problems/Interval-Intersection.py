class Solution:
    def solve(self, intervals):
        ma, mi = float('-inf'), float('inf')
        for i in intervals:
            if i[0] > ma:
                ma = i[0]
            if i[1] < mi:
                mi = i[1]
        return [ma, mi]
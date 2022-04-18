class Solution:
    def solve(self, intervals, point):
        count = 0
        for i in intervals:
            if i[0] <= point and point <= i[1]:
                count+=1
        return count
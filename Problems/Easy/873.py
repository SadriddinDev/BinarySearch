import math
class Solution:
    def solve(self, nums, k, target):
        s = sum(nums)
        return math.ceil(abs(target - s)/abs(k))
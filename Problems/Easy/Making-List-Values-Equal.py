class Solution: # v1
    def solve(self, nums):
        return max(nums) - min(nums)

class Solution: #v2
    def solve(self, nums):
        mi, ma = float("inf"), float('-inf')
        for i in nums:
            if i > ma:
                ma = i
            if i < mi:
                mi = i
        return ma - mi
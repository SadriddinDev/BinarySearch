class Solution:
    def solve(self, nums):
        new = sorted(nums)
        c = 0
        for i in range(len(nums)):
            c+=nums[i] == new[i]
        return c
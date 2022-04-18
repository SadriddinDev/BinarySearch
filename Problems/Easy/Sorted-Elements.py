class Solution:
    def solve(self, nums):
        new_nums = sorted(nums)
        c = 0
        for i in range(len(nums)):
            c+=nums[i] == new_nums[i]
        return c
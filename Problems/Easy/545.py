class Solution:
    def solve(self, nums):
        nums.sort()
        return [nums[i//2] if i % 2 else nums[-(i//2+1)] for i in range(len(nums))]
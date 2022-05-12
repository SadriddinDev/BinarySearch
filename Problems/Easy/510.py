class Solution:
    def solve(self, nums):
        if len(nums) < 2:
            return 0
        c = 0

        for i in range(1, len(nums)-1):
            if not (nums[i-1] >= nums[i] >= nums[i+1]) and not (nums[i-1] <= nums[i] <= nums[i+1]):
                c += 1
        return c

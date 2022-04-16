class Solution:
    def solve(self, nums):
        nums.sort()
        d = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > d:
                d = nums[i+1]-nums[i]
        return d
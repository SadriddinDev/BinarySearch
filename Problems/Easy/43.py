class Solution:
    def solve(self, nums, k):
        k = k % len(nums)
        if k == 0:
            return nums
        return nums[k:] + nums[:k]

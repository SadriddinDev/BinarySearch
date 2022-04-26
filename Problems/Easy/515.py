class Solution:
    def solve(self, nums, k):
        l = len(nums)-1
        s = sum(nums)
        for i in nums:
            if (s - i)/l == k:
                return True
        return False
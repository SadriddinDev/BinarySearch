class Solution:# v1
    def solve(self, nums):
        max1, max2 = 0, 0
        index = 0
        for i in range(len(nums)):
            if nums[i] > max1:
                max1 = nums[i]
                index = i
        for i in range(len(nums)):
            if nums[i] > max2 and i!=index:
                max2 = nums[i]
        return max2 *2 < max1

class Solution: # v2
    def solve(self, nums):
        nums.sort()
        return nums[-2] * 2 < nums[-1]

class Solution: # v3
    def solve(self, nums):
        n = len(nums)
        first, second = float("-inf"), float("-inf")
        for i in nums:
            if i >= first:
                first, second = i, first
            elif i > second:
                second = i 
        return second * 2 < first
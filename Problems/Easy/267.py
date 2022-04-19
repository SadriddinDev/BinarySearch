class Solution:
    def solve(self, nums):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if not nums[i] % 2 and not nums[j] % 2:
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                elif nums[i] % 2 and nums[j] % 2:
                    if nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
        return nums

class Solution:
    def solve(self, nums):
        for i in range(0, len(nums)-2, 4):
            nums[i], nums[i+2] = nums[i+2], nums[i]
        for i in range(1, len(nums)-2, 4):
            nums[i], nums[i+2] = nums[i+2], nums[i]
        return nums


class Solution:
    def solve(self, nums):
        LL = len(nums)
        for i in range(0, len(nums)-2, 4):
            nums[i], nums[i+2] = nums[i+2], nums[i]
            if i < LL - 3:
                nums[i+1], nums[i+3] = nums[i+3], nums[i+1]
        return nums

class Solution:
    def solve(self, nums):
        if len(nums) < 2:
            return []
        peaks = []
        n = len(nums)
        for i in range(len(nums)):
            if i > 0 and i < n-1:
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                    peaks.append(i)
            elif i == 0 and nums[i] > nums[i+1]:
                peaks.append(i)
            elif i == len(nums) - 1 and nums[i] > nums[i-1]:
                peaks.append(i)
        return peaks

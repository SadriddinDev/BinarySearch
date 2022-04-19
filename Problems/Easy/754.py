class Solution: # v1
    def solve(self, nums):
        nums.sort()
        dif = nums[1] - nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != dif:
                return False
        return True


class Solution: # best version
    def solve(self, nums):
        minima = min(nums)
        maxima = max(nums)

        d = (maxima - minima) / (len(nums) - 1)
        num = minima + d
        nums_set = set(nums)
        if d == 0:
            return True
        while num in nums_set:
            num += d

        if num > maxima:
            return True
        return False
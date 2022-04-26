class Solution:
    def solve(self, nums):
        l = nums.__len__()
        cond = True
        for i in range(l//2):
            if i*2 + 1 < l:
                cond = cond and nums[i] >= nums[2*i+1]
            if i*2 + 2 < l:
                cond = cond and nums[i] >= nums[2*i+2]
        return cond

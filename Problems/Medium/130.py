class Solution:
    def solve(self, nums):
        nums = sorted(list(set(nums)))
        c = 0
        m = 0
        l = float("-inf")
        for i in nums:
            if l == i-1:
                c += 1
            else:
                if m < c:
                    m = c
                c = 1
            l = i
        if m < c:
            m = c
        return m
class Solution:
    def solve(self, nums):
        mset = set(nums)
        c = 0
        for i in nums:
            c += (i+1) in mset
        return c

class Solution:
    def solve(self, nums):
        Hash = {}
        for i in nums:
            Hash[i] = True
        c = 0
        for i in nums:
            c += Hash.get(i+1, 0)
        return c
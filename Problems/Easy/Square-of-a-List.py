class Solution:
    def solve(self, nums):
        l = 0
        r = len(nums)-1
        i = r
        mlist = [0]*len(nums)
        while i>=0:
            if abs(nums[l]) > abs(nums[r]):
                mlist[i] = nums[l]*nums[l]
                l+=1 
            else:
                mlist[i] = nums[r]*nums[r]
                r-=1
            i-=1
        return mlist
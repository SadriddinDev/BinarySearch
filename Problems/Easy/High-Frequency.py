class Solution:
    def solve(self, nums):
        mdict = {}
        m = 0
        for num in nums:
            if mdict.get(num):
                mdict[num]+=1
            else:
                mdict[num]=1
            if mdict[num]>m:
                m = mdict[num]
        return m
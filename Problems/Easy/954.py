class Solution:
    def solve(self, nums):
        c = 0
        l = None
        for i in nums:
            if i == 1:
                if l != 1:
                    c+=1
                    l = 1
                    if c > 1:
                        return False
            l = i
        return c == 1
                

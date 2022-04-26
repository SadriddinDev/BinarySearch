import math
class Solution:
    def solve(self, nums):
        return math.gcd(*nums)


class Solution:
    def solve(self, nums):
        def ekub(a, b):
            while a != b:
                if a == 0:
                    return b
                if b == 0:
                    return a
                if a > b:
                    a = a % b
                else:
                    b = b % a
            return a
        e = nums[0]
        for i in nums[1:]:
            e = ekub(i, e)
        return e
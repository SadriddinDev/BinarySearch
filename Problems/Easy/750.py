class Solution:
    def solve(self, n):
        if n < 2:
            return True
        low = 1
        high = n
        mid = (low + high) // 2
        while True:
            if mid ** 2 == n:
                return True
            elif mid ** 2 > n:
                if high == mid:
                    return False
                high = mid
            else:
                if low == mid:
                    return False
                low = mid
            mid = (low+high)//2

class Solution:
    def solve(self, n):
        l, h = 0, n
        while l <= h:
            mid = (l + h) >> 1
            tot = mid ** 2
            if tot == n:
                return True
            elif tot < n:
                l = mid + 1
            else:
                h = mid - 1
        return False
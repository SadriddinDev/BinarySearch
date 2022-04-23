class Solution:
    def solve(self, n):
        low = 0
        high = n
        while low < high:
            mid = (low + high)//2
            kv = mid * mid
            if kv <= n and (mid+1) * (mid+1) > n:
                return mid
            elif kv > n:
                high = mid
            else:
                low = mid
        return mid

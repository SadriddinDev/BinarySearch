class Solution:
    def solve(self, nums):
        low = 0
        high = len(nums)-1
        ans = []
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == mid:
                ans.append(mid)
            if nums[mid] < mid:
                low = mid + 1
            else:
                high = mid - 1
        if len(ans) > 0:
            return min(ans)
        return -1

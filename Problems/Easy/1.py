from collections import defaultdict


class Solution:
    def solve(self, nums, k):
        Hash = defaultdict(int)
        for i in nums:
            Hash[i] += 1
            if Hash[k-i]:
                if k-i == i:
                    if Hash[i] > 1:
                        return True
                else:
                    return True
        return False

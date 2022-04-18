class Solution:
    def solve(self, prices, k):
        prices.sort()
        c = 0
        budget = 0
        for p in prices:
            budget+=p
            if budget<=k:
                c+=1
            else:
                break
        return c
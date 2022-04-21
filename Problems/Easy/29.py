class Solution:
    def solve(self, s):
        ans = ""
        last = ""
        for i in s:
            if last != i:
                last = i
                ans += last
        return ans
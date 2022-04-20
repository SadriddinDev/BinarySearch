class Solution: # v1
    def solve(self, s):
        l = True
        r = True
        c = False
        for i in s:
            if i == "B" and not c:
                l = False
            elif i == 'R':
                c = True
            elif c and i == "B":
                r = False
        return l or r

class Solution:
    def solve(self, s):
        left, right = s.split("R")
        return left.find("B") == -1 or right.find("B") == -1 
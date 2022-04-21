class Solution:
    def solve(self, s):
        o = 0
        for i in s:
            if i == "(":
                o+=1
            else:
                if o == 0:
                    return False
                else:
                    o-=1
        return o == 0
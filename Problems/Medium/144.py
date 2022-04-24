class Solution:
    def solve(self, lst, p):
        l = lst[:]
        for i in range(len(lst)):
            lst[p[i]] = l[i]
        return lst

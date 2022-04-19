class Solution:
    def solve(self, votes):
        mdict = {}
        for i in votes:
            if i[1] in mdict:
                return True
            mdict[i[1]] = True
        return False


class Solution: # best solution
    def solve(self, votes):
        voted = [x for i, x in votes]
        set_voted = set(voted)
        if len(votes) != len(set_voted):
            return True
        return False
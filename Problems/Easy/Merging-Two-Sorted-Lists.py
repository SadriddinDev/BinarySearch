class Solution: # v1
    def solve(self, a, b):
        i = 0
        j = 0
        mlist = []
        while i < len(a) or j < len(b):
            if i < len(a):
                if j < len(b):
                    if a[i] < b[j]:
                        mlist.append(a[i])
                        i+=1
                    else:
                        mlist.append(b[j])
                        j+=1
                else:
                    mlist.append(a[i])
                    i+=1
            else:
                mlist.append(b[j])
                j+=1
        return mlist

class Solution: # v2
    def solve(self, a, b):
        mlist = a + b
        return sorted(mlist)
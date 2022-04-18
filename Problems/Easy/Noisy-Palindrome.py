class Solution:
    def solve(self, s):
        i = 0
        j = len(s)-1

        while i < j:
            if s[i].islower():
                if s[j].islower():
                    if s[i] == s[j]:
                        i += 1
                        j -= 1
                    else:
                        return False
                else:
                    j-=1
            else:
                i+=1
        return True
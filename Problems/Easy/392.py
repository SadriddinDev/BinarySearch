class Solution:
    def solve(self, s):
        bracket_list = []
        b_s = ""
        o_count = 0
        n = len(s)
        for i in range(n):
            b_s += s[i]
            if s[i] == "(":
                o_count += 1
            else:
                o_count -= 1
                if o_count == 0 or i == n-1:
                    bracket_list.append(b_s)
                    b_s = ""
        return bracket_list


class Solution:# v2
    def solve(self, s):
        bracket_list = []
        b_s = ""
        o_count = 0
        for c in s:
            b_s += c
            if c == "(":
                o_count += 1
            else:
                o_count -= 1
                if o_count == 0:
                    bracket_list.append(b_s)
                    b_s = ""
        return bracket_list
                
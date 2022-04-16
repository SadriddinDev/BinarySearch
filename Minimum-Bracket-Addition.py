class Solution:
    def solve(self, s):
        open_count = 0
        need_count = 0
        for i in s:
            if i == ")":
                if not open_count:
                    need_count += 1
                else:
                    open_count -= 1
            else:
                open_count += 1
        return need_count + open_count
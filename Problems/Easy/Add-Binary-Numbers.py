class Solution: # 1
    def solve(self, a, b):
        return bin(int(a, 2)+int(b, 2))[2:]

class Solution: # 2
    def solve(self, a, b):
        n_1 = 0
        n_2 = 0
        for i in a:
            n_1 = n_1 * 2 + int(i)
        for i in b:
            n_2 = n_2 * 2 + int(i)
        n_3 = n_1 + n_2
        ans = "" if n_3 > 0 else "0"
        while n_3 > 0:
            ans = str(n_3%2) + ans
            n_3 = n_3 // 2
        return ans
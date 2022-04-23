class Solution:
    def solve(self, x, y):
        c = 0
        while x or y:
            if x and y:
                c += (x % 2 != y % 2)
                x = x // 2
                y = y // 2
            elif x:
                if x % 2 == 1:
                    c += 1
                x //= 2
            else:
                if y % 2 == 1:
                    c += 1
                y //= 2
        return c

class Solution:
    def solve(self, x, y):
        return bin(x ^ y).count("1")
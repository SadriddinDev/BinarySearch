# power of 2 will be like this: 1, 10, 100 ... (one 1 and other zero)
# so we should check one count
class Solution:
    def solve(self, n):
        one_count = 0
        while n:
            one_count += n % 2
            n //= 2
        return one_count == 1
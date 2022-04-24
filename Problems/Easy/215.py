class Solution:
    def solve(self, n):
        cache = set()

        def nums_square(number):
            s = 0
            while number:
                s = s + (number % 10)**2
                number //= 10
            return s
        while n:
            n = nums_square(n)
            if n == 1:
                return True
            if n in cache:
                return False
            cache.add(n)

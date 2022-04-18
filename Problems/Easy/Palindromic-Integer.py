class Solution:
    def solve(self, num):
        d = 1
        while d <= num:
            d *= 10
        d /=10
        d2 = 10
        print(d)
        while d2 <= d:
            print((num%d2)/(d2/10), (num%(d*10))//d)
            if (num%d2)//(d2/10) != (num%(d*10))//d:
                return False
            d2 *=10
            d /=10
        return True

print(Solution().solve(100))

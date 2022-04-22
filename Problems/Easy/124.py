class Solution:
    def solve(self, n):
        if n == 0:
            return [1]
        elif n == 1:
            return [1, 1]
        temp = [1, 1]
        c = 2
        while c <= n:
            new = []
            for i in range(len(temp)-1):
                new.append(temp[i] + temp[i+1])
            temp = [1] + new + [1]
            c += 1
        return temp 

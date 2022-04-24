class Solution:
    def solve(self, path):
        paths = []
        for i in path:
            if i == "..":
                if paths:
                    paths.pop()
            elif i != ".":
                paths.append(i)
        return paths

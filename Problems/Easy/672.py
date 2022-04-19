class Solution:  # v1
    def solve(self, matrix):
        m = [[0 if n else 1 for n in row] for row in matrix]
        for i in range(len(m)):
            n = len(m[i])
            for j in range(n//2):
                m[i][j], m[i][-(j+1)] = m[i][-(j+1)], m[i][j]
        return m


class Solution:  # v2
    def solve(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = 0 if matrix[i][j] else 1

        for i in range(len(matrix)):
            n = len(matrix[i])
            for j in range(n//2):
                matrix[i][j], matrix[i][-(j+1)] = matrix[i][-(j+1)], matrix[i][j]
        return matrix


class Solution:  # v2 best solution
    def solve(self, matrix):
        result = []
        for row in matrix:
            rev_row = row[::-1]
            new_row = [0 if val else 1 for val in rev_row]
            result.append(new_row)
        return result


class Solution:  # v2 best solution
    def solve(self, matrix):
        return [[0 if val else 1 for val in row[::-1]] for row in matrix]

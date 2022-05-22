class Solution:
    def solve(self, matrix):
        max_row_list = []
        max_col_list = []
        for i in matrix:
            max_row_list.append(max(i))
        n = len(matrix)
        m = 0
        if n > 0:
            m = len(matrix[0])
        for i in range(m):
            colm = float("-inf")
            for j in range(n):
                if matrix[j][i] > colm:
                    colm = matrix[j][i]
            max_col_list.append(colm)
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] >= max_row_list[i] and matrix[i][j] >= max_col_list[j]:
                    count += 1
        return count

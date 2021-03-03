'''
矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
'''
from typing import List
'''
思路：从设置2个数组，分别记录需要更新为0的行、列
时间复杂度：O(m*n)
空间复杂度：O(m+n)
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = 0 if m == 0 else len(matrix[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(m):
            if row[i]:
                for j in range(n):
                    matrix[i][j] = 0
        for i in range(n):
            if col[i]:
                for j in range(m):
                    matrix[j][i] = 0


s = Solution()
a = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(s.setZeroes(a))
print(a)
a = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(s.setZeroes(a))
print(a)
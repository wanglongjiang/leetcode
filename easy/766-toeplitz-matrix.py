'''
托普利茨矩阵

给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

'''
from typing import List
'''
解题思路:遍历第1行以及第1列的元素,向右下搜索是否有不同元素
'''


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        # 第1行元素向右下搜索
        for i in range(col - 1):
            j = 0
            while i + 1 < col and j + 1 < row:
                if matrix[j][i] != matrix[j + 1][i + 1]:
                    return False
                i += 1
                j += 1
        # 第1列元素向右下搜索
        for i in range(1, row - 1):
            j = 0
            while i + 1 < row and j + 1 < col:
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
                i += 1
                j += 1
        return True


s = Solution()
print(s.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(s.isToeplitzMatrix([[1, 2], [2, 2]]))

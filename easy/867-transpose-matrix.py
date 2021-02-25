'''
转置矩阵

给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。

矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
'''

from typing import List
'''
思路：简单问题，原矩阵大小为m*n，创建一个n*m大小的新矩阵，按照行列转化的方式将旧矩阵数据复制过去
'''


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        newMatrix = [[]] * n
        for i in range(n):
            newMatrix[i] = [0] * m
            for j in range(m):
                newMatrix[i][j] = matrix[j][i]
        return newMatrix


s = Solution()
print(s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.transpose([[1, 2, 3], [4, 5, 6]]))

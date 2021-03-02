'''
二维区域和检索 - 矩阵不可变
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
'''
from typing import List
'''
思路：动态规划
设置一个辅助二维数组m*n，每个元素存储从0，0到该点的所有元素和
子矩阵的和为子矩阵右下角的值，加上上左上角的值、减去右上角的值、减去左下角的值
'''


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix) + 1
        n = 1 if m == 1 else len(matrix[0]) + 1
        self.sums = [[0] * n for i in range(m)]
        sums = self.sums
        for i in range(m - 1):
            for j in range(n - 1):
                sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] + matrix[i][j] - sums[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] + self.sums[row1][col1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1]


s = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(s.sumRegion(2, 1, 4, 3))
print(s.sumRegion(1, 1, 2, 2))
print(s.sumRegion(1, 2, 2, 4))
print(s.sumRegion(0, 0, 0, 0))
print(s.sumRegion(1, 1, 1, 1))

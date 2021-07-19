'''
面试题 01.08. 零矩阵
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

 

示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
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

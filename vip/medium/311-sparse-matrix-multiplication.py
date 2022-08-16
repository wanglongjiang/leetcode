'''
311. 稀疏矩阵的乘法
给你两个 稀疏矩阵 A 和 B，请你返回 AB 的结果。你可以默认 A 的列数等于 B 的行数。

请仔细阅读下面的示例。



示例：

输入：

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

输出：

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''
from typing import List
'''
思路：数学 矩阵乘法
按照矩阵乘法的定义，计算2个矩阵的乘法

时间复杂度：O(mnk)，m为矩阵a的行，n为矩阵b的列，k为矩阵a、b的列、行
空间复杂度：O(1)，除返回值，不需要其他额外空间，新矩阵的大小为矩阵a的行*矩阵b的列，也就是m*n
'''


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not mat1 or not mat2:
            return [[]]
        m, n, o = len(mat1), len(mat2[0]), len(mat1[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(o):
                    ans[i][j] += mat1[i][k] * mat2[k][j]
        return ans


s = Solution()
print(s.multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]]))

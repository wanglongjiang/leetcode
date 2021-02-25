'''
旋转图像

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''

from typing import List
'''
思路：
模拟旋转过程，把矩阵看成多个圈，从外圈到内圈依次旋转
模拟旋转过程，查看矩阵最上面2个元素的旋转坐标变化：
0,0->0,n-1->n-1,n-1->n-1,0->0,0
0,1->1,n-1->n-1,n-1-1->n-1-1,0->0,1
可以得到下面的变化规律
row,col -> col,n-1-row -> n-1-row,n-1-col->n-1-col,row->row,col
把矩阵看成多个圈，从外圈到内圈依次旋转
时间复杂度：O(n*n)
空间复杂度：O(1)
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mt = matrix
        n = len(mt)
        r = n - 1
        # 矩阵只有n//2圈需要旋转, 每条直线上只需要旋转n-1个记录，
        for i in range(n // 2):
            c = n - i - 1
            for j in range(i, c):
                tup = mt[r - j][i], mt[i][j], mt[j][r - i], mt[r - i][r - j]
                mt[i][j], mt[j][r - i], mt[r - i][r - j], mt[r - j][i] = tup
        return matrix


s = Solution()
print(
    s.rotate([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35,
                                                                                                                                        36]]))
print(s.rotate([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))
print(s.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.rotate([[1]]))
print(s.rotate([[1, 2], [3, 4]]))

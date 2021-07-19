'''
面试题 01.07. 旋转矩阵
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？

 

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
注意：本题与主站 48 题相同：https://leetcode-cn.com/problems/rotate-image/
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
        mt = matrix
        n = len(mt)
        r = n - 1
        # 矩阵只有n//2圈需要旋转, 每条直线上只需要旋转n-1个记录，
        for i in range(n // 2):
            c = n - i - 1
            for j in range(i, c):
                tup = mt[r - j][i], mt[i][j], mt[j][r - i], mt[r - i][r - j]
                mt[i][j], mt[j][r - i], mt[r - i][r - j], mt[r - j][i] = tup

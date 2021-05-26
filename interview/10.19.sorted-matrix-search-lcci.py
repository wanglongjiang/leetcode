'''
面试题 10.09. 排序矩阵查找
给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
'''
from typing import List
'''
思路：二分查找
> 与主站240.[搜索二维矩阵 II](medium/240-search-a-2d-matrix-ii.py) 相同

对比矩阵target是否介于左上和右下之间，如果是，对比矩阵中点元素。
> 如果与中点元素相同，返回True
> 如果比中点元素小，将矩阵缩小为中点左上部分。
> 如果比中点元素大，搜索中点下方的矩阵和右侧的矩阵。

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # 搜索矩阵指定范围
        def binSearch(top, left, bottom, right):
            if matrix[top][left] > target:
                return False
            if matrix[bottom][right] < target:
                return False
            if (bottom - top + 1) * (right - left + 1) <= 8:  # 如果矩阵少于8个元素，直接查找
                for i in range(top, bottom + 1):
                    for j in range(left, right + 1):
                        if matrix[i][j] == target:
                            return True
                return False
            # 矩阵元素多于8个，二分查找
            vmid, hmid = (top + bottom) // 2, (left + right) // 2
            if matrix[vmid][hmid] == target:
                return True
            if matrix[vmid][hmid] > target:  # 比中点小，搜索中点左上的矩阵
                return binSearch(top, left, vmid, hmid)
            # 比中点大，搜索中点下方的矩阵和右侧矩阵
            if vmid + 1 < m and binSearch(vmid + 1, left, bottom, right):
                return True
            if hmid + 1 < n and binSearch(top, hmid + 1, vmid, right):
                return True
            return False

        return binSearch(0, 0, m - 1, n - 1)

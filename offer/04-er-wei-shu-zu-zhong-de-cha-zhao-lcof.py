'''
剑指 Offer 04. 二维数组中的查找

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

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

 

限制：

0 <= n <= 1000

0 <= m <= 1000

 

注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
'''
from typing import List
'''
思路：二分查找
对比矩阵target是否介于左上和右下之间，如果是，对比矩阵中点元素。
> 如果与中点元素相同，返回True
> 如果比中点元素小，搜索中点上部和左部的矩阵。
> 如果比中点元素大，搜索中点下方的矩阵和右侧的矩阵。

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
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
            if matrix[vmid][hmid] > target:  # 比中点小，搜索上部，左部的矩阵
                if vmid > top:
                    if binSearch(top, left, vmid, right):
                        return True
                else:
                    if binSearch(top, left, vmid, hmid):
                        return True
                if hmid > left:
                    if binSearch(top, left, bottom, hmid):
                        return True
                else:
                    if binSearch(top, left, vmid, hmid):
                        return True
                return False
            # 比中点大，搜索中点下方的矩阵和右侧矩阵
            if vmid + 1 < m and binSearch(vmid + 1, left, bottom, right):
                return True
            if hmid + 1 < n and binSearch(top, hmid + 1, vmid, right):
                return True
            return False

        return binSearch(0, 0, m - 1, n - 1)


s = Solution()
print(s.findNumberIn2DArray([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
print(s.findNumberIn2DArray([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 5))
print(s.findNumberIn2DArray([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))

'''
1901. 找出顶峰元素 II
一个 2D 网格中的 顶峰元素 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。

给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。
找出 任意一个 顶峰元素 mat[i][j] 并 返回其位置 [i,j] 。

你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。

要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法





示例 1:



输入: mat = [[1,4],[3,2]]
输出: [0,1]
解释: 3和4都是顶峰元素，所以[1,0]和[0,1]都是可接受的答案。
示例 2:



输入: mat = [[10,20,15],[21,30,14],[7,16,32]]
输出: [1,1]
解释: 30和32都是顶峰元素，所以[1,1]和[2,2]都是可接受的答案。


提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
任意两个相邻元素均不相等.
'''
from typing import List
'''
思路：二分查找
如果宽度超过高度，二分查找列
如果高度超过宽度，二分查找行
首先假设是宽度超过高度，取中间列，找到该列最大值，
> 如果该最大值也大于左右2列，那么就是顶峰（因为相邻单元格都不同）
> 如果左边值更大，二分查找左边的矩阵
> 如果右边值更大，二分查找右边的矩阵
重复以上过程，直至发现顶峰

时间复杂度：O(mlogn) or O(nlogm)
空间复杂度：O(1)
'''


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(mat[0]) - 1, 0, len(mat) - 1
        while True:
            if right - left > bottom - top:  # 宽度超过高度，二分查找宽度
                mid = (right + left) // 2
                maxIdx = top
                for i in range(top, bottom + 1):  # 查找中间列，最大值的行索引
                    if mat[i][mid] > mat[maxIdx][mid]:
                        maxIdx = i
                if (mid == left or mat[maxIdx][mid] > mat[maxIdx][mid - 1]) and (mid == right or mat[maxIdx][mid] > mat[maxIdx][mid + 1]):
                    return [maxIdx, mid]
                elif mid > left and mat[maxIdx][mid] < mat[maxIdx][mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 高度超过宽度，二分查找高度
                mid = (bottom + top) // 2
                maxIdx = left
                for i in range(left, right + 1):  # 查找中间行，最大值的列索引
                    if mat[mid][i] > mat[mid][maxIdx]:
                        maxIdx = i
                if (mid == top or mat[mid][maxIdx] > mat[mid - 1][maxIdx]) and (mid == bottom or mat[mid][maxIdx] > mat[mid + 1][maxIdx]):
                    return [mid, maxIdx]
                elif mid > top and mat[mid][maxIdx] < mat[mid - 1][maxIdx]:
                    bottom = mid - 1
                else:
                    top = mid + 1


s = Solution()
print(s.findPeakGrid([[1, 4], [3, 2]]))
print(s.findPeakGrid([[10, 20, 15], [21, 30, 14], [7, 16, 32]]))

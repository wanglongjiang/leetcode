'''
1292. 元素和小于等于阈值的正方形的最大边长
给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。

请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
 

示例 1：



输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。
示例 2：

输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
输出：0
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 300
0 <= mat[i][j] <= 104
0 <= threshold <= 105 
'''

from typing import List
'''
思路：前缀和
设置一个与输入矩阵相同大小的辅助矩阵，保存从0,0开始的矩阵和
遍历每个坐标，利用前缀和计算以其为右下角的正方形矩阵和是否满足题意

时间复杂度：O(mn*min(m,n))
空间复杂度：O(mn)
'''


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        pmat = [[0] * n for _ in range(m)]
        # 计算矩阵前缀和
        for i in range(m):
            for j in range(n):
                left, top, leftTop = 0, 0, 0
                if j > 0:
                    left = pmat[i][j - 1]
                if i > 0:
                    top = pmat[i - 1][j]
                if i > 0 and j > 0:
                    leftTop = pmat[i - 1][j - 1]
                pmat[i][j] = mat[i][j] + left + top - leftTop
        ans = 0
        # 计算每个点与其左上构成的正方形矩阵和是否满足要求
        for i in range(m):
            for j in range(n):
                for width in range(ans + 1, min(i + 2, j + 2)):  # 正方形的边长从ans开始
                    if i - width < -1 or j - width < -1:  # 检查正方形是否越界
                        break
                    left, top, leftTop = 0, 0, 0
                    if i - width >= 0:
                        left = pmat[i - width][j]
                    if j - width >= 0:
                        top = pmat[i][j - width]
                    if i - width >= 0 and j - width >= 0:
                        leftTop = pmat[i - width][j - width]
                    s = pmat[i][j] - left - top + leftTop  # 计算出正方形的和
                    if s <= threshold:
                        ans = width
                    else:  # 和超过阈值，不用再扩大范围
                        break
        return ans


s = Solution()
print(s.maxSideLength(mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], threshold=4))
print(s.maxSideLength(mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], threshold=1))

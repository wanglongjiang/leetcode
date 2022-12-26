'''
1139. 最大的以 1 为边界的正方形
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

 

示例 1：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9
示例 2：

输入：grid = [[1,1,0,0]]
输出：1
 

提示：

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] 为 0 或 1
'''
from typing import List
'''
思路：前缀和
首先统计每行，每列的前缀和
然后遍历所有的单元格，
对于i,j，以其为右下角的正方形，边长设为k，如果(i,j),(i-k,j),(i,j-k)处的行、列前缀和均>=k，则有一个大小为k的正方形。

时间复杂度：O(mn*min(m,n))
空间复杂度：O(mn)
'''


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 计算行、列上的前缀和
        rowsum, colsum = [row.copy() for row in grid], [row.copy() for row in grid]
        for i in range(m):
            for j in range(1, n):
                if rowsum[i][j]:
                    rowsum[i][j] += rowsum[i][j - 1]
        for i in range(1, m):
            for j in range(n):
                if colsum[i][j]:
                    colsum[i][j] += colsum[i - 1][j]
        # 找到最大的正方形
        ans = 0
        for i in range(m):
            for j in range(ans, n):
                for k in range(max(1, ans), min(rowsum[i][j], colsum[i][j]) + 1):
                    if rowsum[i - k + 1][j] >= k and colsum[i][j - k + 1] >= k:
                        ans = max(ans, k)
        return ans * ans


s = Solution()
assert s.largest1BorderedSquare([[1, 1, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 9
print(s.largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(s.largest1BorderedSquare([[1, 1, 0, 0]]))

'''
1594. 矩阵的最大非负积
给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。

在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积 的路径。
路径的积是沿路径访问的单元格中所有整数的乘积。

返回 最大非负积 对 109 + 7 取余 的结果。如果最大积为负数，则返回 -1 。

注意，取余是在得到最大积之后执行的。

 

示例 1：

输入：grid = [[-1,-2,-3],
             [-2,-3,-3],
             [-3,-3,-2]]
输出：-1
解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1
示例 2：

输入：grid = [[1,-2,1],
             [1,-2,1],
             [3,-4,1]]
输出：8
解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)
示例 3：

输入：grid = [[1, 3],
             [0,-4]]
输出：0
解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)
示例 4：

输入：grid = [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]
输出：2
解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)
 

提示：

1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4
'''
from typing import List
'''
思路：动态规划
到达m-1,n-1的最大乘积路径，与grid[m-1][n-1]的值正负相关，
如果grid[m-1][n-1]是正数，那么取之前路径的最大值，否则取最小值。

可以用动态规划，设maxdp[m][n]，mindp[m][n]，分别保存截止i,j的最大乘积和最小乘积，状态转移方程为：
maxdp[i][j] = max(maxdp[i - 1][j] * grid[i][j], maxdp[i][j - 1] * grid[i][j], mindp[i - 1][j] * grid[i][j], mindp[i][j - 1] * grid[i][j])
mindp[i][j] = min(mindp[i - 1][j] * grid[i][j], mindp[i][j - 1] * grid[i][j], maxdp[i - 1][j] * grid[i][j], maxdp[i][j - 1] * grid[i][j])


时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxdp, mindp = [[0] * n for i in range(m)], [[0] * n for i in range(m)]
        maxdp[0][0] = mindp[0][0] = grid[0][0]
        for i in range(1, m):
            maxdp[i][0] = maxdp[i - 1][0] * grid[i][0]
            mindp[i][0] = mindp[i - 1][0] * grid[i][0]
        for j in range(1, n):
            maxdp[0][j] = maxdp[0][j - 1] * grid[0][j]
            mindp[0][j] = mindp[0][j - 1] * grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                maxdp[i][j] = max(maxdp[i - 1][j] * grid[i][j], maxdp[i][j - 1] * grid[i][j], mindp[i - 1][j] * grid[i][j], mindp[i][j - 1] * grid[i][j])
                mindp[i][j] = min(mindp[i - 1][j] * grid[i][j], mindp[i][j - 1] * grid[i][j], maxdp[i - 1][j] * grid[i][j], maxdp[i][j - 1] * grid[i][j])
        return maxdp[m - 1][n - 1] % (10**9 + 7) if maxdp[m - 1][n - 1] >= 0 else -1


s = Solution()
print(s.maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]))
print(s.maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]))
print(s.maxProductPath([[1, 3], [0, -4]]))
print(s.maxProductPath([[1, 4, 4, 0], [-2, 0, 0, 1], [1, -1, 1, 1]]))

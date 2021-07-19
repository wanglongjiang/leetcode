'''
剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200
'''
from typing import List
'''
思路：动态规划
设动态规划二维数组dp[m][n]，m为grid.length,n为grid[0].length
dp[i][j]的意思是在grid[i][j]处，能获得的最大价值
因为只能向下，向右移动，所以很容易得到动态规划转移方程为：
dp[i][j]=max(dp[i-1][j],dp[i][j-1])+grid[i][j]

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 增加1行和1列，简化算法
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[m][n]

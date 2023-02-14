'''
1463. 摘樱桃 II
困难
64
相关企业
给你一个 rows x cols 的矩阵 grid 来表示一块樱桃地。 grid 中每个格子的数字表示你能获得的樱桃数目。

你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 (0,0) 出发，机器人 2 从右上角格子 (0, cols-1) 出发。

请你按照如下规则，返回两个机器人能收集的最多樱桃数目：

从格子 (i,j) 出发，机器人可以移动到格子 (i+1, j-1)，(i+1, j) 或者 (i+1, j+1) 。
当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。
当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。
两个机器人在任意时刻都不能移动到 grid 外面。
两个机器人最后都要到达 grid 最底下一行。
 

示例 1：



输入：grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
输出：24
解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
机器人 1 摘的樱桃数目为 (3 + 2 + 5 + 2) = 12 。
机器人 2 摘的樱桃数目为 (1 + 5 + 5 + 1) = 12 。
樱桃总数为： 12 + 12 = 24 。
示例 2：



输入：grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
输出：28
解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
机器人 1 摘的樱桃数目为 (1 + 9 + 5 + 2) = 17 。
机器人 2 摘的樱桃数目为 (1 + 3 + 4 + 3) = 11 。
樱桃总数为： 17 + 11 = 28 。
示例 3：

输入：grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
输出：22
示例 4：

输入：grid = [[1,1],[1,1]]
输出：4
 

提示：

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100 
'''
from typing import List
'''
[TOC]

# 思路
动态规划

# 解题方法

设数组dp[rows][cols][cols]，dp[i][j][k]2个机器人在第i行，第j、k列所能得到的最大樱桃数，状态转移方程为：
> dp[i][j][k] = max(dp[i-1][j-1..j+1][k-1..k+1])+grid[i][j]+grid[i][k]

# 复杂度
- 时间复杂度: 
> $O(rows*cols*cols)$ 

- 空间复杂度: 
> $O(rows*cols*cols)$
'''


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]
        # 初始化
        dp[0][0][cols - 1] = grid[0][0] + grid[0][cols - 1]
        # dp计算
        for i in range(1, rows):
            for j in range(min(cols, i)):
                for k in range(max(j + 1, cols - i - 1), cols):
                    # 遍历2个机器人前一坐标所有的可能
                    for col1, col2 in [(col1, col2) for col1 in range(j - 1, j + 2) if 0 <= col1 < cols for col2 in range(k - 1, k + 2) if 0 <= col2 < cols]:
                        if col1 == col2:
                            continue
                        dp[i][j][k] = max(dp[i][j][k], grid[i][j] + grid[i][k] + dp[i - 1][col1][col2])
        return max(max(dp[-1][j]) for j in range(cols))


s = Solution()
assert s.cherryPickup(grid=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0], [1, 0, 2, 3, 0, 0, 6]]) == 28
assert s.cherryPickup([[0, 8, 7, 10, 9, 10, 0, 9, 6], [8, 7, 10, 8, 7, 4, 9, 6, 10], [8, 1, 1, 5, 1, 5, 5, 1, 2], [9, 4, 10, 8, 8, 1, 9, 5, 0],
                       [4, 3, 6, 10, 9, 2, 4, 8, 10], [7, 3, 2, 8, 3, 3, 5, 9, 8], [1, 2, 6, 5, 6, 2, 0, 10, 0]]) == 96
assert s.cherryPickup([[4, 1, 5, 7, 1], [6, 0, 4, 6, 4], [0, 9, 6, 3, 5]]) == 32
assert s.cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]) == 24
assert s.cherryPickup(grid=[[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]) == 22
assert s.cherryPickup(grid=[[1, 1], [1, 1]]) == 4

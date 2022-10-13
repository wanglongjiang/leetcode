'''
2435. 矩阵中和能被 K 整除的路径
给你一个下标从 0 开始的 m x n 整数矩阵 grid 和一个整数 k 。你从起点 (0, 0) 出发，每一步只能往 下 或者往 右 ，你想要到达终点 (m - 1, n - 1) 。

请你返回路径和能被 k 整除的路径数目，由于答案可能很大，返回答案对 109 + 7 取余 的结果。

 

示例 1：



输入：grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
输出：2
解释：有两条路径满足路径上元素的和能被 k 整除。
第一条路径为上图中用红色标注的路径，和为 5 + 2 + 4 + 5 + 2 = 18 ，能被 3 整除。
第二条路径为上图中用蓝色标注的路径，和为 5 + 3 + 0 + 5 + 2 = 15 ，能被 3 整除。
示例 2：


输入：grid = [[0,0]], k = 5
输出：1
解释：红色标注的路径和为 0 + 0 = 0 ，能被 5 整除。
示例 3：


输入：grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], k = 1
输出：10
解释：每个数字都能被 1 整除，所以每一条路径的和都能被 k 整除。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 5 * 104
1 <= m * n <= 5 * 104
0 <= grid[i][j] <= 100
1 <= k <= 50
'''
from typing import List
'''
思路：动态规划
设三维数组dp[m][n][k]，dp[i][j][l]的意思是经过gird[i][j]，路径和mod(k)==l的路径数量。
状态转移方程为：dp[i][j][ki] = dp[i-1][j][x]+dp[i][j-1][x] 其中(x+grid[i][j])%k==ki，即x=ki-gird[i][j]%k

时间复杂度：O(mnk)
空间复杂度：O(mnk)
'''


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        modular = 10**9 + 7
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1  # 初始化第0，0个单元格经过的路径和计数
        for i in range(1, n):
            for j in range(k):
                dp[0][i][j] = dp[0][i - 1][j - grid[0][i] % k] % modular  # 计算第0行各个单元格路径和计数
        for i in range(1, m):
            for j in range(k):
                dp[i][0][j] = dp[i - 1][0][j - grid[i][0] % k] % modular  # 计算第0列各个单元格路径和计数
        for i in range(1, m):
            for j in range(1, n):
                for ki in range(k):
                    dp[i][j][ki] = (dp[i - 1][j][ki - grid[i][j] % k] + dp[i][j - 1][ki - grid[i][j] % k]) % modular  # 计算第i,j个单元格路径和计数
        return dp[-1][-1][0]


s = Solution()
print(s.numberOfPaths(grid=[[5, 2, 4], [3, 0, 5], [0, 7, 2]], k=3))
print(s.numberOfPaths(grid=[[0, 0]], k=5))
print(s.numberOfPaths(grid=[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], k=1))

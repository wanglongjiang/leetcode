'''
1931. 用三种不同颜色为网格涂色
困难
39
相关企业
给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。

涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 109 + 7 取余 的结果。

 

示例 1：


输入：m = 1, n = 1
输出：3
解释：如上图所示，存在三种可能的涂色方案。
示例 2：


输入：m = 1, n = 2
输出：6
解释：如上图所示，存在六种可能的涂色方案。
示例 3：

输入：m = 5, n = 5
输出：580986
 

提示：

1 <= m <= 5
1 <= n <= 1000
'''
'''
[TOC]

# 思路
动态规划

# 解题方法

设数组dp[m][n][3]，dp[i][j][0]是当前单元格为红色时的方案数，dp[i][j][1]是当前单元格为绿色时的方案数，dp[i][j][2]是蓝色时的方案数。

状态转移方程为：
- dp[i][j][0] = (dp[i-1][j][1]+dp[i-1][j][2])*(dp[i][j-1][1]+dp[i][j-1][2])
- dp[i][j][1] = (dp[i-1][j][0]+dp[i-1][j][2])*(dp[i][j-1][0]+dp[i][j-1][2])
- dp[i][j][2] = (dp[i-1][j][1]+dp[i-1][j][0])*(dp[i][j-1][1]+dp[i][j-1][0])
最后结果为sum(dp[m-1][n-1])


# 复杂度
- 时间复杂度: 
> $O(mn)$ 

- 空间复杂度: 
> $O(mn)$
'''


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        dp = [[[0] * 3 for _ in range(n)] for _ in range(m)]
        MOD = 10**9 + 7
        dp[0][0][0], dp[0][0][1], dp[0][0][2] = 1, 1, 1
        for i in range(1, m):
            dp[i][0][0] = dp[i - 1][0][1] + dp[i - 1][0][2]
            dp[i][0][1] = dp[i - 1][0][0] + dp[i - 1][0][2]
            dp[i][0][2] = dp[i - 1][0][0] + dp[i - 1][0][1]
        for j in range(1, n):
            dp[0][j][0] = dp[0][j - 1][1] + dp[0][j - 1][2]
            dp[0][j][1] = dp[0][j - 1][0] + dp[0][j - 1][2]
            dp[0][j][2] = dp[0][j - 1][0] + dp[0][j - 1][1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j][0] = ((dp[i - 1][j][1] + dp[i - 1][j][2]) * (dp[i][j - 1][1] + dp[i][j - 1][2])) % MOD
                dp[i][j][1] = ((dp[i - 1][j][0] + dp[i - 1][j][2]) * (dp[i][j - 1][0] + dp[i][j - 1][2])) % MOD
                dp[i][j][2] = ((dp[i - 1][j][1] + dp[i - 1][j][0]) * (dp[i][j - 1][1] + dp[i][j - 1][0])) % MOD
        return sum(dp[m - 1][n - 1]) % MOD


s = Solution()
assert s.colorTheGrid(m=5, n=5) == 580986
assert s.colorTheGrid(m=1, n=2) == 6
assert s.colorTheGrid(m=1, n=1) == 3
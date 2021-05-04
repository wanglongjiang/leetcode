'''
粉刷房子 III
在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。
有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。

我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，
它包含 5 个街区  [{1}, {2,2}, {3,3}, {2}, {1,1}] 。）

给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：

houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区。如果没有可用的涂色方案，请返回 -1 。

示例 1：

输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：9
解释：房子涂色方案为 [1,2,2,1,1]
此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
示例 2：

输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：11
解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
示例 3：

输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
输出：5
示例 4：

输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
输出：-1
解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。
 

提示：

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
'''
from typing import List
'''
思路：暴力计算
1、确定有几个分区exists：遍历所有的houses，如果当前房子不为0，且与上一个房子颜色不一样则exists+1
2、如果exists>target，返回-1；如果exists==target，未刷漆房子与2边房子对比，选择便宜的颜色粉刷；
    如果exists<target，需要执行下面的3：创建新的街区
3、统计未粉刷的房子，加入数组unpainted，每个未粉刷的房子尝试每种颜色，
然后统计街区数量==target的方案中，花费最少的1个
时间复杂度：O(m^n)
空间复杂度：O(n)

思路2：动态规划
3维动态规划数组，dp[i,j,k]表示第i个房子，第j+1个街区(从1开始），颜色为k+1（从1开始）时的最小费用
答案是min(dp[m-1,target,n])
时间复杂度：O(m*n*n)
空间复杂度：O(m*n*n)
'''


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf')] * n for _ in range(target + 1)] for _ in range(m)]
        if houses[0]:  # 第0个房子已经粉刷，成本为0
            dp[0][1][houses[0] - 1] = 0
        else:  # 第0个房子未粉刷，需要依次遍历第0个房子粉刷各个颜色的成本进行初始化
            for i in range(1, n + 1):
                dp[0][1][i - 1] = cost[0][i - 1]
        for i in range(1, m):  # 遍历所有房子
            for j in range(1, target + 1):  # 所有街区
                for k in range(1, n + 1):  # 所有颜色
                    c = float('inf')
                    for col in range(1, n + 1):
                        if col != k:
                            c = min(c, dp[i - 1][j - 1][col - 1])  # 计算与上一个房子少一个街区的颜色
                    c = min(c, dp[i - 1][j][k - 1])  # 从与上一个房子相同街区，少一个街区的中选择较少的作为成本基数
                    # 只有当前房子未粉刷颜色，或者已粉刷的颜色与k相同，才是合法的粉刷方案
                    if houses[i] == 0:
                        dp[i][j][k - 1] = c + cost[i][k - 1]
                    elif houses[i] == k:
                        dp[i][j][k - 1] = c
        # 返回答案
        ans = min(dp[m - 1][target][:])
        if ans == float('inf'):
            return -1
        else:
            return ans


s = Solution()
print(s.minCost(houses=[0, 0, 0, 0, 0], cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], m=5, n=2, target=3))
print(s.minCost(houses=[0, 2, 1, 2, 0], cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], m=5, n=2, target=3))
print(s.minCost(houses=[0, 0, 0, 0, 0], cost=[[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]], m=5, n=2, target=5))
print(s.minCost(houses=[3, 1, 2, 3], cost=[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], m=4, n=3, target=3))

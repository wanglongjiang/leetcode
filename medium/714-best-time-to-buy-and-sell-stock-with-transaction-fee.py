'''
买卖股票的最佳时机含手续费
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
'''
from typing import List
'''
思路：动态规划
设dp[i][j]，j=1 or 0,dp[i][0]指在第i天买入股票的收益，dp[i][1]指在第i天持有股票的收益,dp[i][2]指在第i天卖出股票的收益
动态规划状态转移方程为：
dp[i][0] = dp[i - 1][2] # 买入时的收益等于上次卖出时的收益
dp[i][1] = max(dp[i - 1][1] + prices[i] - prices[i - 1], dp[i - 1][0] + prices[i] - prices[i - 1], dp[i-1][2]) # 持有时的收益为上次持有+这2天的收益，或者上次买入+这2天的收益，或者当天买入
dp[i][2] = max(dp[i - 1][2], dp[i][1] - fee)

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][2]
            dp[i][1] = max(dp[i - 1][1] + prices[i] - prices[i - 1], dp[i - 1][0] + prices[i] - prices[i - 1], dp[i - 1][2])
            dp[i][2] = max(dp[i - 1][2], dp[i][1] - fee)
        return dp[n - 1][2]


s = Solution()
print(s.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
print(s.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))

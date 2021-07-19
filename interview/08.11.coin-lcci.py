'''
面试题 08.11. 硬币
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000
'''
'''
思路：动态规划
这是一个完全背包问题。
状态转移方程为：dp[j] = dp[j] + dp[j-coins[i]]
状态转移方程的含义是，金额为j时的兑换组合数=已知的组合数+金额为j-coins[i]时的组合数

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25, 10, 5, 1]
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], n + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[n]


s = Solution()
print(s.waysToChange(6))
print(s.waysToChange(5))
print(s.waysToChange(10))

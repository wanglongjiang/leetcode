'''
零钱兑换 II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1
 

注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数
'''
from typing import List
'''
思路：动态规划 完全背包问题
这个题目是个典型的完全背包问题，用动态规划写出算法。
状态转移方程为：dp[j] = dp[j] + dp[j-coins[i]]
状态转移方程的含义是，金额为j时的兑换组合数=已知的组合数+金额为j-coins[i]时的组合数

时间复杂度：O(amount*n)
空间复杂度：O(amount)
'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]


s = Solution()
print(s.change(amount=5, coins=[1, 2, 5]))
print(s.change(amount=3, coins=[2]))
print(s.change(amount=10, coins=[10]))

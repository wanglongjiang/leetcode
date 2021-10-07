'''
剑指 Offer II 103. 最少的硬币数目
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 23^1 - 1
0 <= amount <= 10^4
 

注意：本题与主站 322 题相同： https://leetcode-cn.com/problems/coin-change/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gaM7Ch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：动态规划
完全背包问题，
设dp[i]为截止第i元钱，最少需要的硬币个数
状态转移方程为
dp[i]=min(dp[i], dp[i-coins[j]]+1)
意思是针对dp[i]需要遍历所有的零钱金额，其兑换次数是dp[i-零钱面额]+1

时间复杂度：O(n*amount)
空间复杂度：O(amount)
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

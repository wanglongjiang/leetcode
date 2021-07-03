'''
第 N 个泰波那契数
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

 

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：

输入：n = 25
输出：1389537
 

提示：

0 <= n <= 37
答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
'''
from functools import lru_cache
'''
思路1：递归 记忆化搜索
使用函数的定义写出递归函数
使用记忆化搜索进行优化

时间复杂度：O(n)
空间复杂度：O(n)

思路2：动态规划
设dp[i]为第i个泰波那契数
状态转移方程为：
dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    # 思路2，动态规划
    def tribonacci(self, n: int) -> int:
        dp = [0] * max(n + 1, 3)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]

    # 思路1，记忆化搜到
    @lru_cache
    def tribonacci1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

'''
斐波那契数
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3
 

提示：

0 <= n <= 30
'''
from functools import lru_cache
'''
思路1：递归 记忆化搜索
按照定义写出结果

时间复杂度：O(n)
空间复杂度：O(n)

思路2：动态规划
状态转移方程为
dp[i] = dp[i-1]+dp[i-2]

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    # 思路2 动态规划
    def fib(self, n: int) -> int:
        dp = [0] * max(n + 1, 2)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # 思路1 记忆化搜索
    @lru_cache
    def fib1(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


s = Solution()
print(s.fib(4))
print(s.fib(30))

'''
整数拆分

给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
'''
'''
思路：动态规划
设dp[i]为长度为i的绳子经过剪切后的最大乘积，状态转移方程为：
dp[i] = max(dp[j]*(i-j))，j为小于i的所有绳子
dp[1] = 1
经过一个2重迭代，可以计算出如上dp数组，最后结果是dp[n]

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j), j * (i - j))
        return dp[n]


s = Solution()
print(s.integerBreak(6))
print(s.integerBreak(2))
print(s.integerBreak(10))

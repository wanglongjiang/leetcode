'''
完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：

输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
 
提示：

1 <= n <= 10^4
'''
'''
思路：动态规划 背包问题
用背包问题的思路解决，将n设置为背包大小

时间复杂度：O(n*sqrt(n))
空间复杂度：O(n)
'''


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)  # 最坏情况下由n个1构成
        dp[0] = 0
        dp[1] = 1
        if n > 1:
            dp[2] = 2
        if n > 2:
            dp[3] = 3
        for i in range(2, int(n**0.5) + 1):
            square = i * i
            for j in range(square, n + 1):
                dp[j] = min(dp[j], dp[j - square] + 1)
        return dp[n]


s = Solution()
print(s.numSquares(6))
print(s.numSquares(12))
print(s.numSquares(13))

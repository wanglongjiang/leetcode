'''
剑指 Offer 14- I. 剪绳子

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
'''
'''
思路：动态规划
设dp[i]为长度为i的绳子经过剪切后的最大乘积，状态转移方程为：
dp[i] = max(dp[j]*(i-j))，j为小于i的所有绳子
dp[0] = 1
经过一个2重迭代，可以计算出如上dp数组，最后结果是dp[n]

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j), j * (i - j))
        return dp[n] % 1000000007


s = Solution()
print(s.cuttingRope(120))
print(s.cuttingRope(2))
print(s.cuttingRope(10))

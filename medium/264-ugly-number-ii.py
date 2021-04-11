'''
丑数 II
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。
'''
'''
思路1，调用上题的函数，时间复杂度:超过O(n^2)
思路2，动态规划
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]


s = Solution()
print(s.nthUglyNumber(10))
print(s.nthUglyNumber(1690))

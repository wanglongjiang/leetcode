'''
剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

提示：

0 <= n <= 100
'''
'''
解题思路：数学里面的组合
n需要分解成x个1和y个2，x最大为n，最小为n%2，y最小为0，最大为n//2，每种组合都有(x+y)!/(x!*y!)个

'''


class Solution:
    def numWays(self, n: int) -> int:
        import math
        ans = 0
        for twoNum in range(n // 2 + 1):
            oneNum = n - (twoNum << 1)
            ans += math.factorial(twoNum + oneNum) // (math.factorial(twoNum) * math.factorial(oneNum))
        return ans % 1000000007


s = Solution()
print(s.numWays(2))
print(s.numWays(5))
print(s.numWays(0))
print(s.numWays(7))

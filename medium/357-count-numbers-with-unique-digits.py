'''
计算各个位数不同的数字个数
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。

示例:

输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
'''
from functools import reduce
'''
思路：数学 动态规划
n为1时，为10
n为2时，为个位数0..9+两位数的组合9*9（意思是十位数可能的取值为1..9，个位数的取值为0..9并且与十位数不同），
根据上面分析得到动态转移方程
dp[i]=dp[i-1]+9*(10-1)*..*(10-i+1)

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n > 10:
            n = 10  # 超过10位数，肯定会有重复的数字，因此最大就到10位数
        dp = [0] * (n + 2)
        dp[0], dp[1] = 1, 10
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + 9 * reduce(lambda a, b: a * b, range(9, 10 - i, -1), 1)
        return dp[n]


s = Solution()
print(s.countNumbersWithUniqueDigits(1))
print(s.countNumbersWithUniqueDigits(2))
print(s.countNumbersWithUniqueDigits(3))
print(s.countNumbersWithUniqueDigits(4))
print(s.countNumbersWithUniqueDigits(5))
print(s.countNumbersWithUniqueDigits(6))
print(s.countNumbersWithUniqueDigits(7))
print(s.countNumbersWithUniqueDigits(8))
print(s.countNumbersWithUniqueDigits(9))
print(s.countNumbersWithUniqueDigits(10))
print(s.countNumbersWithUniqueDigits(11))

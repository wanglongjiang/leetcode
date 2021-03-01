'''
爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
'''
'''
解题思路：数学里面的组合
n需要分解成x个1和y个2，x最大为n，最小为n%2，y最小为0，最大为n//2，每种组合都有(x+y)!/(x!*y!)个
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        ans = 0
        for twoNum in range(n // 2 + 1):
            oneNum = n - (twoNum << 1)
            ans += math.factorial(twoNum + oneNum) // (math.factorial(twoNum) * math.factorial(oneNum))
        return ans


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))

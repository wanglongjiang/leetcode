'''
吃掉 N 个橘子的最少天数
厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：

吃掉一个橘子。
如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
每天你只能从以上 3 种方案中选择一种方案。

请你返回吃掉所有 n 个橘子的最少天数。

提示：

1 <= n <= 2*10^9
'''
'''
思路1，暴力回溯
如果n能被3整除，有2种吃法：1个、2n/3个
如果n能被2整除，有2种吃法：1个，n/2个
如果n能同时被2、3整除，有3种吃法：1个，n/2个，2n/3个
回溯函数eat(n)=1+min(eat(n-1),eat(n/2),eat(n/3))
时间复杂度：O(n)
空间复杂度：O(3^n)

思路2，
TODO
'''


class Solution:
    # 思路1，暴力回溯
    def minDays(self, n: int) -> int:
        dp = {}  # 记忆化

        def eat(x):
            if x in dp:
                return dp[x]
            if x == 1:
                return 1
            if x % 3 == 0 and x % 2 == 0:
                count = min(eat(x // 3), eat(x // 2), eat(x - 1))
            elif x % 3 == 0:
                count = min(eat(x // 3), eat(x - 1))
            elif x % 2 == 0:
                count = min(eat(x // 2), eat(x - 1))
            else:
                count = eat(x - 1)
            dp[x] = count + 1
            return dp[x]

        return eat(n)


s = Solution()
print(s.minDays(3**5))
print(s.minDays(8))
print(s.minDays(9))
print(s.minDays(10))
print(s.minDays(6))
print(s.minDays(1))
print(s.minDays(56))

'''
猜数字大小 II
我们正在玩一个猜数游戏，游戏规则如下：

我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。

每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。

然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。

示例:

n = 10, 我选择了8.

第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。

游戏结束。8 就是我选的数字。

你最终要支付 5 + 7 + 9 = 21 块钱。
给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。
'''
'''
思路：动态规划

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(2, n + 1):
            for i in range(j - 1, -1, -1):
                global_min = float('inf')
                for k in range(i + 1, j):
                    global_min = min(global_min, k + max(dp[i][k - 1], dp[k + 1][j]))
                dp[i][j] = i if i + 1 == j else global_min  # 当i == j - 1时，dp[i][j]即为i j中的较小者i
        return dp[1][n]


s = Solution()
print(s.getMoneyAmount(10))

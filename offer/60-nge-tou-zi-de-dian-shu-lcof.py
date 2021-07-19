'''
剑指 Offer 60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
 

限制：

1 <= n <= 11
'''
from typing import List
'''
思路1，暴力排列
每个骰子有6个面，n个骰子的排列数是6^n，暴力统计这些排列的值的计数。然后值的计数除以总计数得到概率。
时间复杂度：O(6^n)，超时了
空间复杂度：O(6^n)

思路2，动态规划
设二维数组dp[n][k]为动态规划数组，n>0，k=6n，也就是n个骰子最大点数就是6n
dp[i][j]的含义是有i个骰子，投掷出点数为j时的次数。
状态转移方程为:
dp[i][j] = dp[i-1][j-1]+dp[i-1][j-2]+dp[i-1][j-3]+dp[i-1][j-4]+dp[i-1][j-5]+dp[i-1][j-6]
意思是投掷第i个骰子要在第i-1个骰子基础上进行，点数j-1..j-6的都能到达点数j的，所以点数j的为j-1+..+j-6的总和
初始值
dp[1][1..6]=1

时间复杂度：O(6n^2)
空间复杂度：O(6n^2)
'''


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [[0] * (6 * n + 1) for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1  # 初始值
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j - 2] + dp[i - 1][j - 3] + dp[i - 1][j - 4] + dp[i - 1][j - 5] + dp[i - 1][j - 6]
        k = 6 * n - n + 1  # n个骰子可能的点数和的数量
        ans = [0] * k
        total = sum(dp[n])
        for i in range(k):
            ans[i] = dp[n][i + n] / total
        return ans


s = Solution()
print(s.dicesProbability(1))
print(s.dicesProbability(2))

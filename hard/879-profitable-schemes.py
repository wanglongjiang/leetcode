'''
盈利计划
集团里有 n 名员工，他们可以完成各种各样的工作创造利润。

第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。

工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。

有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。

 

示例 1：

输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
输出：2
解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
总的来说，有两种计划。
示例 2：

输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
输出：7
解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
 

提示：

1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
'''
from typing import List
'''
思路：二维背包问题，用dp解决
典型的二维背包问题，这里将最小利润和总计人数作为状态

时间复杂度：O(nmk)，m为minProfit,k为group.length
空间复杂度：O(nm)
'''


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]  # 以利润和人数作为状态
        dp[0][0] = 1  # 利润和人数均为0的方案数只有1个
        for i in range(len(group)):  # 按照套路，遍历所有的价值（利润、人数）
            for j in range(minProfit, -1, -1):  # 按照套路，遍历所有的利润状态
                p = min(minProfit, j + profit[i])  # 超过了最小利润要求，按照最小利润算
                for k in range(n - group[i], -1, -1):  # 遍历所有的合法人数
                    dp[p][k + group[i]] = dp[p][k + group[i]] + dp[j][k]  # 通常的二维背包状态方程是取max，这里是求所有方案，需要相加
        return sum(dp[minProfit]) % 1000000007


s = Solution()
print(s.profitableSchemes(n=5, minProfit=3, group=[2, 2], profit=[2, 3]))
print(s.profitableSchemes(n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8]))

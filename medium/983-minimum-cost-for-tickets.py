'''
983. 最低票价
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。
每一项是一个从 1 到 365 的整数。

火车票有三种不同的销售方式：

一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：
第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。



示例 1：

输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。
示例 2：

输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
输出：17
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。
你总共花了 $17，并完成了你计划的每一天旅行。


提示：

1 <= days.length <= 365
1 <= days[i] <= 365
days 按顺序严格递增
costs.length == 3
1 <= costs[i] <= 1000
'''
from typing import List
'''
思路：动态规划
设二维数组dp[n][3]，dp[i][j]的意思是第i天，购买第j种票的花费。
状态转移方程为：
* dp[i][0] = min(dp[i-1][0],dp[i-1][1],dp[i-1][2])，意思是如果第i天购买第1种票（1天有效期），最低花费为1天前的最小值。
* dp[i][1] = min(dp[i-7][0],dp[i-7][1],dp[i-7][2])，意思是如果第i天购买第2种票（7天有效期），最低花费为7天前的最小值。
* dp[i][2] = min(dp[i-30][0],dp[i-30][1],dp[i-30][2])，意思是如果第i天购买第3种票（30天有效期），最低花费为30天前的最小值。

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [[0] * 3 for _ in range(n)]
        for i, d in enumerate(days):
            dp[i][0] = min(dp[i - 1]) + costs[0] if i > 0 else costs[0]  # 购买1天票的花费是1天前最低花费+1天票价
            k = i - 1
            while k >= 0 and d - days[k] < 7:  # 找到7天前的日期索引k
                k -= 1
            dp[i][1] = min(dp[k]) + costs[1] if k >= 0 else costs[1]  # 购买7天票的花费是7天前最低花费+7天票价
            k = i - 1
            while k >= 0 and d - days[k] < 30:  # 找到30天前的日期索引k
                k -= 1
            dp[i][2] = min(dp[k]) + costs[2] if k >= 0 else costs[2]  # 购买30天票的花费是30天前最低花费+30天票价
        return min(dp[n - 1])


s = Solution()
print(s.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
print(s.mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))
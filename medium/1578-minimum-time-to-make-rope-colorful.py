'''
1578. 使绳子变成彩色的最短时间
Alice 把 n 个气球排列在一根绳子上。给你一个下标从 0 开始的字符串 colors ，其中 colors[i] 是第 i 个气球的颜色。

Alice 想要把绳子装扮成 彩色 ，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 彩色 。
给你一个下标从 0 开始的整数数组 neededTime ，其中 neededTime[i] 是 Bob 从绳子上移除第 i 个气球需要的时间（以秒为单位）。

返回 Bob 使绳子变成 彩色 需要的 最少时间 。

 

示例 1：


输入：colors = "abaac", neededTime = [1,2,3,4,5]
输出：3
解释：在上图中，'a' 是蓝色，'b' 是红色且 'c' 是绿色。
Bob 可以移除下标 2 的蓝色气球。这将花费 3 秒。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 3 。
示例 2：


输入：colors = "abc", neededTime = [1,2,3]
输出：0
解释：绳子已经是彩色的，Bob 不需要从绳子上移除任何气球。
示例 3：


输入：colors = "aabaa", neededTime = [1,2,3,4,1]
输出：2
解释：Bob 会移除下标 0 和下标 4 处的气球。这两个气球各需要 1 秒来移除。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 1 + 1 = 2 。
 

提示：

n == colors.length == neededTime.length
1 <= n <= 105
1 <= neededTime[i] <= 104
colors 仅由小写英文字母组成
'''
from typing import List
'''
思路：贪心
找出连续相同的气球，保留时间最大的1个即可

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, n = 1, len(colors)
        ans = 0
        while i < n:
            if colors[i - 1] == colors[i]:  # 找到联系相同的颜色
                maxTime, sumTime = neededTime[i - 1], neededTime[i - 1]
                while i < n and colors[i - 1] == colors[i]:
                    sumTime += neededTime[i]
                    maxTime = max(maxTime, neededTime[i])
                    i += 1
                ans += sumTime - maxTime
            else:
                i += 1
        return ans


s = Solution()
print(s.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
print(s.minCost(colors="abc", neededTime=[1, 2, 3]))
print(s.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))

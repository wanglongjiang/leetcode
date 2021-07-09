'''
最佳观光组合
给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。

一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。

返回一对观光景点能取得的最高分。

 

示例 1：

输入：values = [8,1,5,2,6]
输出：11
解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
示例 2：

输入：values = [1,2]
输出：2
 

提示：

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-sightseeing-pair
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：动态规划
从题目中知道，截止当前索引j，最大观光组合为：values[i] + values[j] + i - j
上面的公式里，values[j]-j是固定值，values[i]+i需要从j前面寻找，
因为values[i]+i不会发生变化，对于索引j来说，要么在j-1之前，要么是j-1。
故可以写出状态转移方程：
dp[j]=max(dp[j-1], values[j-1]+j-1)，这里的dp[j]意思是截止索引j，最大的values[i]+i
初始值：
dp[0]=0
ans = values[j]-j+dp[j]

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = float('-inf')
        dp = [0] * len(values)
        for i in range(1, len(values)):
            dp[i] = max(dp[i - 1], values[i - 1] + i - 1)
            ans = max(ans, values[i] - i + dp[i])
        return ans


s = Solution()
print(s.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
print(s.maxScoreSightseeingPair([1, 2]))
print(s.maxScoreSightseeingPair([2, 0]))

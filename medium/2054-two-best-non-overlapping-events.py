'''
2054. 两个最好的不重叠活动
给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。
第 i 个活动开始于 startTimei ，结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。
你 最多 可以参加 两个时间不重叠 活动，使得它们的价值之和 最大 。

请你返回价值之和的 最大值 。

注意，活动的开始时间和结束时间是 包括 在活动时间内的，也就是说，
你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。
更具体的，如果你参加一个活动，且结束时间为 t ，那么下一个活动必须在 t + 1 或之后的时间开始。

 

示例 1:



输入：events = [[1,3,2],[4,5,2],[2,4,3]]
输出：4
解释：选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。
示例 2：

Example 1 Diagram

输入：events = [[1,3,2],[4,5,2],[1,5,5]]
输出：5
解释：选择活动 2 ，价值和为 5 。
示例 3：



输入：events = [[1,5,3],[1,5,1],[6,6,5]]
输出：8
解释：选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。
 

提示：

2 <= events.length <= 105
events[i].length == 3
1 <= startTimei <= endTimei <= 109
1 <= valuei <= 106
'''
from bisect import bisect_left
from typing import List
'''
思路：排序 二分查找
1、将events按照startTime从小到大排序
2、创建后缀数组maxVals，对于每个元素maxVals[i]，保存i之后最大的value
3、遍历events，根据endTime二分查找与其不相交的最近事件，如果存在，设其下标为j，再查看maxVals[j]的值，events[i][2]+maxVals[j]即为事件i的得分

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda e: e[0])
        maxVals = [0] * n
        maxVals[-1] = events[-1][2]
        for i in range(n - 2, -1, -1):
            maxVals[i] = max(maxVals[i + 1], events[i][2])  # 创建最大值的后缀数组
        startTimes = [e[0] for e in events]  # 提取出时间开始时间，便于二分查找
        ans = 0
        for i, e in enumerate(events):
            j = bisect_left(startTimes, e[1] + 1, i + 1)  # 二分查找与e不相交的事件
            if j < n:
                ans = max(ans, e[2] + maxVals[j])
            else:
                ans = max(ans, e[2])
        return ans

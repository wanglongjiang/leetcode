'''
最多可以参加的会议数目
给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。

你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。

请你返回你可以参加的 最大 会议数目。

 

示例 1：



输入：events = [[1,2],[2,3],[3,4]]
输出：3
解释：你可以参加所有的三个会议。
安排会议的一种方案如上图。
第 1 天参加第一个会议。
第 2 天参加第二个会议。
第 3 天参加第三个会议。
示例 2：

输入：events= [[1,2],[2,3],[3,4],[1,2]]
输出：4
示例 3：

输入：events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
输出：4
示例 4：

输入：events = [[1,100000]]
输出：1
示例 5：

输入：events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
输出：7
 

提示：

1 <= events.length <= 10^5
events[i].length == 2
1 <= events[i][0] <= events[i][1] <= 10^5
'''
from typing import List
import heapq
'''
思路：贪心算法 堆 排序
对会议按照开始日期进行排序，然后参加会议：
> 开始日期不同的，先使用开日期较小的，
> 开始日期相同的，先使用快结束的（结束日期较小的），然后将其他相同开始日期的推迟一天。

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heap = list(map(lambda e: (e[0], e[1]), events))  # 会议由数组转化为元组，便于按照开始日期、结束日期进行排序
        heapq.heapify(heap)  # 进行堆排序
        ans = 0
        while heap:
            ans += 1
            e = heapq.heappop(heap)
            while heap and e[0] == heap[0][0]:  # 如果最近的会议与当前会议开始时间相同，需要推迟一天或放弃
                if heap[0][0] < heap[0][1]:  # 如果会议开始时间小于结束时间，推迟一天
                    heapq.heapreplace(heap, (heap[0][0] + 1, heap[0][1]))
                else:  # 如果会议开始时间、结束时间相同，无法推迟，需要放弃
                    heapq.heappop(heap)
        return ans


s = Solution()
print(s.maxEvents([[1, 2], [2, 3], [3, 4]]))
print(s.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))
print(s.maxEvents([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))
print(s.maxEvents([[1, 100000]]))
print(s.maxEvents([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]))

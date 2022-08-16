'''
会议室 II
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，
为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

 

示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：2
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：1
 

提示：

1 <= intervals.length <= 10^4
0 <= starti < endi <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：差分数组
设一个大小为max(intervals[0..n][1])的数组arr，默认为0
遍历每个时间区间，arr[开始时间]+1，arr[结束时间+1]-1
然后再次遍历arr,找到最大值

时间复杂度：O(max(intervals))
'''


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        size = 0
        for interval in intervals:
            size = max(size, interval[1])
        arr = [0] * (size + 2)
        for interval in intervals:
            arr[interval[0]] += 1
            arr[interval[1] + 1] -= 1
        ans, val = 0, 0
        for v in arr:
            val += v
            ans = max(ans, val)
        return ans


s = Solution()
print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(s.minMeetingRooms([[7, 10], [2, 4]]))

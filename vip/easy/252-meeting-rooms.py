'''
252. 会议室
给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，
请你判断一个人是否能够参加这里面的全部会议。



示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：true


提示：

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti < endi <= 106
'''
from typing import List
'''
思路：排序
按照会议开始时间进行排序，然后判断前后2个会议时间上是否有交集

时间复杂度：O(n$log^n$)
空间复杂度：O(1)
'''


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda inter: inter[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


s = Solution()
print(s.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(s.canAttendMeetings([[7, 10], [2, 4]]))

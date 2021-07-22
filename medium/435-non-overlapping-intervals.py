'''
无重叠区间
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路：贪心
1. 将intervals按照右边界进行排序
2. 设遍历lastRight为intervals[0]的右边界
3. 遍历intervals，如果intervals[i][0]>=lastRight，说明区间i与前面的区间没有重叠，无重叠区间数count+1。这里用到了贪心的思路，因为经过排序后右边界每次都是最小的。
4. 最后返回n-count，即为要删除的区间数量。

时间复杂度：O(n*logn)
空间复杂度：O(1)
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        lastRight = intervals[0][1]
        count = 1
        for i in range(1, n):
            if intervals[i][0] >= lastRight:
                lastRight = intervals[i][1]
                count += 1
        return n - count


s = Solution()
print(s.eraseOverlapIntervals([[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]))
print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
print(s.eraseOverlapIntervals([[1, 2], [2, 3]]))

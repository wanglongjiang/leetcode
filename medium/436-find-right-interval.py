'''
寻找右区间
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。

区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。

返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，
则下标 i 处的值设为 -1 。

 
示例 1：

输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。
示例 2：

输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1, 0, 1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。
示例 3：

输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1, 2, -1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
 

提示：

1 <= intervals.length <= 2 * 10^4
intervals[i].length == 2
-10^6 <= starti <= endi <= 10^6
每个间隔的起点都 不相同
'''
from typing import List
import bisect
'''
思路：排序+二分查找
对区间的副本按照开始坐标进行排序，然后再遍历intervals二分查找符合条件的右侧区间

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # 对区间按照开始坐标进行排序
        starts, indexs = zip(*sorted(zip([i[0] for i in intervals], range(n)), key=lambda item: item[0]))
        ans = []
        for interval in intervals:
            i = bisect.bisect_left(starts, interval[1])  # 二分查找坐标
            if i == n:
                ans.append(-1)
            else:
                ans.append(indexs[i])  # 右侧区间的坐标写入结果
        return ans


s = Solution()
print(s.findRightInterval([[1, 2]]))
print(s.findRightInterval([[3, 4], [2, 3], [1, 2]]))
print(s.findRightInterval([[1, 4], [2, 3], [3, 4]]))

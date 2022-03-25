'''
2187. 完成旅途的最少时间
给你一个数组 time ，其中 time[i] 表示第 i 辆公交车完成 一趟旅途 所需要花费的时间。

每辆公交车可以 连续 完成多趟旅途，也就是说，一辆公交车当前旅途完成后，可以 立马开始 下一趟旅途。每辆公交车 独立 运行，也就是说可以同时有多辆公交车在运行且互不影响。

给你一个整数 totalTrips ，表示所有公交车 总共 需要完成的旅途数目。请你返回完成 至少 totalTrips 趟旅途需要花费的 最少 时间。

 

示例 1：

输入：time = [1,2,3], totalTrips = 5
输出：3
解释：
- 时刻 t = 1 ，每辆公交车完成的旅途数分别为 [1,0,0] 。
  已完成的总旅途数为 1 + 0 + 0 = 1 。
- 时刻 t = 2 ，每辆公交车完成的旅途数分别为 [2,1,0] 。
  已完成的总旅途数为 2 + 1 + 0 = 3 。
- 时刻 t = 3 ，每辆公交车完成的旅途数分别为 [3,1,1] 。
  已完成的总旅途数为 3 + 1 + 1 = 5 。
所以总共完成至少 5 趟旅途的最少时间为 3 。
示例 2：

输入：time = [2], totalTrips = 1
输出：2
解释：
只有一辆公交车，它将在时刻 t = 2 完成第一趟旅途。
所以完成 1 趟旅途的最少时间为 2 。
 

提示：

1 <= time.length <= 10^5
1 <= time[i], totalTrips <= 10^7
'''
from typing import List
'''
思路：二分查找
完成所有旅途的最大时间为maxtime = min(time)*totalTrips，也就是全部由最快的公交完成所有旅途所需要的时间。
最少时间肯定介于[1,maxtime]之间，可以用二分查找法。
每次选定一个时间midtime，然后查看这个时间，所有公交车能够完成的旅途数量。
如果旅途数量<totalTrips，则需要将区间缩小为[midtime, maxtime]；
如果旅途数量>=totalTrips，则需要将区间缩小为[mintime, midtime]；
重复上述过程，如果出现区间无法缩小，则找到了答案：旅途数量<totalTrips时为maxtime，旅途数量>=totalTrips时为mintime

时间复杂度：O(log(min(time)*totalTrips))
空间复杂度：O(1)
'''


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        mintime, maxtime = 1, min(time) * totalTrips
        while True:
            midtime = (mintime + maxtime) // 2
            trips = sum(map(lambda t: midtime // t, time))
            if trips >= totalTrips:
                if maxtime == midtime:
                    return mintime
                maxtime = midtime
            else:
                if mintime == midtime:
                    return maxtime
                else:
                    mintime = midtime


s = Solution()
print(s.minimumTime(time=[1, 2, 3], totalTrips=5))
print(s.minimumTime(time=[2], totalTrips=1))

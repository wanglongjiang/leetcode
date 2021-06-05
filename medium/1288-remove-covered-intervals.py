'''
删除被覆盖区间

给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。

只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。

在完成所有删除操作后，请你返回列表中剩余区间的数目。

 

示例：

输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
 

提示：​​​​​​

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
对于所有的 i != j：intervals[i] != intervals[j]
'''
from typing import List
'''
思路：排序
1. 对区间进行排序，首先按照左边界，如果左边界相同，再按照右边界降序。经过排序的区间，被覆盖的区间肯定在后面。
2. 遍历区间，每一个都向前搜索，如果它没被前面某个区间覆盖，将其加入剩余list。

时间复杂度：O(n^2)，排序需要O(nlogn)，遍历查找需要O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: (item[0], -item[1]))  # 排序
        n = len(intervals)
        remainder = [intervals[0]]
        for i in range(1, n):
            for r in remainder:  # 遍历之前的区间，如果在其范围内跳过，否则加入剩余list
                if r[0] <= intervals[i][0] and r[1] >= intervals[i][1]:
                    break
            else:
                remainder.append(intervals[i])
        return len(remainder)


s = Solution()
print(s.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))

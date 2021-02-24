'''
合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

'''
from typing import List
'''
思路：数组排序后，相邻的区间肯定靠在一起。类似于冒泡，从左向右合并区间，合并后的区间更新掉原值，当与右边无法合并时，加入结果list
时间复杂度：O(nlogn)，有排序nLogn，一次遍历
空间复杂度：O(n)，辅助数组存放返回值，最坏情况下N
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        n = len(intervals)
        for i in range(1, n):
            left, right = intervals[i - 1], intervals[i]
            if left[1] >= right[0]:
                right[0] = left[0]
                right[1] = max(left[1], right[1])
            else:
                result.append(left)
        result.append(intervals[n - 1])
        return result


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [4, 5]]))

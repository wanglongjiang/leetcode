'''
插入区间

给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
'''

from typing import List
'''
解题思路：二分查找
新插入的区间为[left,right]，分别二分查找left，right在区间列表开始位置中的应该插入的索引leftIndex,rightIndex
可能与新区间合并的区间为intervals[leftIndex-1]或intervals[leftIndex]、intervals[rightIndex]之间的区间
然后将区间列表[0-leftIndex]+合并后的区间+区间列表[rightIndex+1]返回
时间复杂度：O(logN) 查找需要使用O(logN)时间
空间复杂度：O(1) 返回值需要使用空间N
'''


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        def search(val: int):
            start, end = 0, len(intervals) - 1
            if end < 0:
                return 0
            while start <= end:
                mid = (start + end) // 2
                if intervals[mid][0] == val:
                    return mid + 1
                elif intervals[mid][0] > val:
                    end = mid - 1
                    if end < start:  # 找不到下一个位置，直接返回当前位置
                        return mid
                else:
                    start = mid + 1
                    if end < start:  # 找不到下一个位置，直接返回当前位置+1
                        return mid + 1
            return abs(start + end) // 2 + abs(start + end) % 2

        leftIndex = search(newInterval[0])
        rightIndex = search(newInterval[1])
        if leftIndex > 0:
            if intervals[leftIndex - 1][1] >= newInterval[0]:
                leftIndex = leftIndex - 1
                newInterval[0] = min(intervals[leftIndex][0], newInterval[0])
        if rightIndex > 0:
            newInterval[1] = max(newInterval[1], intervals[rightIndex - 1][1])
        return intervals[:leftIndex] + [newInterval] + intervals[rightIndex:]


s = Solution()
print(s.insert(intervals=[[1, 5]], newInterval=[0, 0]))
print(s.insert(intervals=[[1, 5]], newInterval=[0, 3]))
print(s.insert(intervals=[], newInterval=[5, 7]))
print(
    s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
             newInterval=[4, 8]))
print(s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(s.insert(intervals=[[1, 5]], newInterval=[2, 3]))
print(s.insert(intervals=[[1, 5]], newInterval=[2, 7]))

'''
绝对差不超过限制的最长连续子数组

给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，
该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

如果不存在满足条件的子数组，则返回 0 。

'''

from typing import List
'''
解决思路：使用滑动窗口法。
4个指针：
i 记录当前字符，也是子数组右边界
left 记录子数组左边界
maxIndex 记录子数组中最大值的索引，如果最大值有多个，指向最后1个
minIndex 记录子数组中最小值的索引，如果最小值有多个，指向最后1个
遍历数组，遇到的值v会有如下条件
nums[minIndex]>=v，minIndex指向i
nums[maxIndex]<=v, maxIndex指向i
如果nums[maxIndex]-nums[minIndex]>limit，
    将此时的子数组长度与maxLen比较、记录
    如果i=minIndex，说明上限超出，需要从maxIndex+1开始搜索至i，
        left = 最后1次差>limit的右边
        maxIndex = 所有差<=limit的最大索引
    如果i=maxIndex，说明下限超出，需要从minIndex+1开始搜索至i，
        left = 最后1次差>limit的右边
        minIndex = 所有差<=limit的最小索引
时间复杂度：最坏情况下遍历数组2次，O(n)
空间复杂度：使用常数个辅助空间，O(1)
'''


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, minIndex, maxIndex = 0, 0, 0
        maxLen = 0
        n = len(nums)
        for i in range(1, n):
            if nums[minIndex] >= nums[i]:
                minIndex = i
            if nums[maxIndex] <= nums[i]:
                maxIndex = i
            if nums[maxIndex] - nums[minIndex] > limit:
                maxLen = max(maxLen, i - left)
                if i == minIndex:
                    left = maxIndex + 1
                    newMaxIndex = left
                    for j in range(maxIndex + 1, i + 1):
                        if abs(nums[j] - nums[i]) <= limit:
                            if nums[newMaxIndex] <= nums[j]:
                                newMaxIndex = j
                        else:
                            left = j + 1
                            newMaxIndex = left
                    maxIndex = newMaxIndex
                elif i == maxIndex:
                    left = minIndex + 1
                    newMinIndex = left
                    for j in range(minIndex + 1, i + 1):
                        if abs(nums[j] - nums[i]) <= limit:
                            if nums[newMinIndex] >= nums[j]:
                                newMinIndex = j
                        else:
                            left = j + 1
                            newMinIndex = left
                    minIndex = newMinIndex
        return max(maxLen, len(nums) - left)


s = Solution()
print(
    s.longestSubarray([
        92, 86, 32, 33, 100, 9, 88, 58, 56, 71, 33, 70, 57, 69, 59, 2, 51, 44,
        22, 34, 63, 4, 83, 54, 74, 3, 8, 89, 46, 75, 18, 76, 17, 18, 34, 36,
        51, 73, 52, 23, 79, 12, 30, 63, 1, 23, 68, 41, 65, 84, 57, 88, 82, 94,
        29, 31, 41, 64, 88, 62
    ], 53))
print(
    s.longestSubarray([
        7, 40, 10, 10, 40, 39, 96, 21, 54, 73, 33, 17, 2, 72, 5, 76, 28, 73,
        59, 22, 100, 91, 80, 66, 5, 49, 26, 45, 13, 27, 74, 87, 56, 76, 25, 64,
        14, 86, 50, 38, 65, 64, 3, 42, 79, 52, 37, 3, 21, 26, 42, 73, 18, 44,
        55, 28, 35, 87
    ], 63))
print(s.longestSubarray([1, 5, 6, 7, 8, 10, 6, 5, 6], 4))
print(s.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3)
print(s.longestSubarray([8, 2, 4, 7], 4) == 2)
print(s.longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4)
print(s.longestSubarray([1, 2, 3, 4, 5, 4, 3, 2], 0) == 1)
print(s.longestSubarray([1, 2, 3, 4, 4, 4, 3, 2], 0) == 3)
print(s.longestSubarray([1, 2, 3, 4, 4, 4, 3, 2, 2, 2, 2], 0) == 4)

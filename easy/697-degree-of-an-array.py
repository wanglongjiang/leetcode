'''
数组的度
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
'''

from typing import List
'''
解题思路：设置一个辅助hashmap，key为nums中出现的每个整数，value为数组，存放该整数出现的次数、最开始出现的下标、
最后出现的下标
第1次遍历nums，统计出每个整数的出现次数、左右下标，整个数组的度degree
第2次遍历辅助hashmap，找出出现次数与degree相同整数，并找出其左右下标差最小的

时间复杂度：2遍扫描，O(n)
空间复杂度：O(n)
'''


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degreeMap = {}
        degree = 0
        # 第1次遍历nums，统计出每个整数的出现次数、左右下标，整个数组的度degree
        for i in range(len(nums)):
            numInfo = None
            if nums[i] in degreeMap:
                numInfo = degreeMap[nums[i]]
            else:
                numInfo = [0, i, 0]
                degreeMap[nums[i]] = numInfo
            numInfo[0] += 1
            numInfo[2] = i
            degree = max(degree, numInfo[0])
        # 第2次遍历辅助hashmap，找出出现次数与degree相同整数，并找出其左右下标差最小的
        minLen = len(nums)
        for v in degreeMap.values():
            if v[0] == degree:
                minLen = min(minLen, v[2] - v[1] + 1)
        return minLen


s = Solution()
print(s.findShortestSubArray([1, 2, 2, 3, 1]))
print(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))

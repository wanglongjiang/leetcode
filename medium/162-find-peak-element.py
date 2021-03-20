'''
寻找峰值
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。
'''
from typing import List
'''
思路1，一次遍历。时间复杂度O(n)
'''


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return 0 if nums[0] > nums[1] else 1
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

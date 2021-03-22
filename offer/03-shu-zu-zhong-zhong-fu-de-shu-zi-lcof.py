'''
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
'''
from typing import List
'''
思路：哈希表判断是否有重复的元素
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        all = set()
        for num in nums:
            if num in all:
                return num
            else:
                all.add(num)

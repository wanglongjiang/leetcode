'''
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

限制：

0 <= 数组长度 <= 50000

 

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
from typing import List
import bisect
'''
思路：二分查找
二分查找target的边界，然后右边界减去左边界

时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIndex = bisect.bisect_left(nums, target)
        if leftIndex >= len(nums) or nums[leftIndex] != target:  # 未找到target，返回
            return 0
        rightIndex = bisect.bisect_right(nums, target)
        return rightIndex - leftIndex

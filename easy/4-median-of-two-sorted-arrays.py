'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        nums = []
        len1 = len(nums1)
        len2 = len(nums2)
        i1 = 0
        i2 = 0
        while i1 < len1 or i2 < len2:
            if i1 >= len1:
                nums.append(nums2[i2])
                i2 += 1
            elif i2 >= len2:
                nums.append(nums1[i1])
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                nums.append(nums2[i2])
                i2 += 1
            else:
                nums.append(nums1[i1])
                i1 += 1
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        if len(nums) % 2 == 1:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid - 1]) / 2


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]) == 2.0)
print(s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
print(s.findMedianSortedArrays([0, 0], [0, 0]) == 0)
print(s.findMedianSortedArrays([], [1]) == 1.0)
print(s.findMedianSortedArrays([1], []) == 1.0)

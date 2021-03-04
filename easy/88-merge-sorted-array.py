'''
合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
'''
from typing import List
'''
思路:原地合并。
如果从小到大合并，需要使用辅助数组，空间复杂度O(m+n)。
因nums1后面已经预留出足够的空间，可以反过来从大到小，每次从2个数组末尾取最大的放到nums1末尾，直至1个数组为空。
空间复杂度：O(1)
时间复杂度：O(m+n)
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        head = m + n - 1
        p1, p2 = m - 1, n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[head] = nums1[p1]
                p1 -= 1
            else:
                nums1[head] = nums2[p2]
                p2 -= 1
            head -= 1
        # nums2剩余元素复制过去
        while p2 >= 0:
            nums1[head] = nums2[p2]
            p2 -= 1
            head -= 1


s = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
print(s.merge(nums1, m=3, nums2=[2, 5, 6], n=3))
print(nums1)
nums1 = [1]
print(s.merge(nums1, m=1, nums2=[], n=0))
print(nums1)

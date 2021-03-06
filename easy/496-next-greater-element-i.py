'''
下一个更大元素 I
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

'''
from typing import List
'''
思路1，暴力查找法，对于nums1中每个元素，先搜索在nums2中的位置，然后向右搜索更大值
    时间复杂度：O(n*n)
    空间复杂度：O(1)
思路2，单调栈，
    1、利用单调栈，查找nums2中每个元素的下一个大值，保存到map里面。
    2、遍历nums1，在map中查找每个元素的下一个大值
    时间复杂度：O(n)
    空间复杂度：O(n)
'''


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextMap = {}
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                nextMap[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in nextMap:
                ans[i] = nextMap[nums1[i]]
        return ans


s = Solution()
print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(s.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))

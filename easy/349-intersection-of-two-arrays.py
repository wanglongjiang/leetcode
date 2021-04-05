'''
两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。
说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
'''
from typing import List
'''
思路：哈希
将数组1加入哈希表，然后依次数组2中元素是否在哈希表中，如果存在输出到结果中，同时删除哈希表中的元素（避免重复）
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Set = set(nums1)
        ans = []
        for num in nums2:
            if num in num1Set:
                ans.append(num)
                num1Set.remove(num)
        return ans


s = Solution()
print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))

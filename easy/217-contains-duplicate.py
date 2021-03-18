'''
存在重复元素
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
'''
from typing import List
'''
思路：哈希表
如果重复的元素出现，返回True
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        allset = set()
        for n in nums:
            if n in allset:
                return True
            allset.add(n)
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
print(s.containsDuplicate([1, 2, 3, 4]))
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

'''
多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
from typing import List
'''
思路：摩尔投票法
第一想法是哈希表统计，这种方式空间复杂度不满足要求。摩尔投票法能满足需求。
摩尔投票法的思路：相同的数字count+1，不同的数字count-1，因为众数>n/2，所以剩到最后的就是众数
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([3, 2, 3]))

'''
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        deleted = 0
        for i in range(len(nums)):
            if val == nums[i]:
                deleted += 1
            elif deleted > 0:
                nums[i - deleted] = nums[i]
        return len(nums) - deleted


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3) == 2)
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5)

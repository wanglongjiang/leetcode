'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num = None
        deleted = 0
        for i in range(len(nums)):
            if num == nums[i]:
                deleted += 1
            else:
                num = nums[i]
                nums[i - deleted] = num
        return len(nums) - deleted


s = Solution()
print(s.removeDuplicates([1, 1, 2]) == 2)
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5)

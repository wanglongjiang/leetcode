'''
移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''
from typing import List
'''
思路，双指针。
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right, n = 0, 0, len(nums)
        for right in range(n):
            if nums[right]:
                nums[left] = nums[right]
                left += 1
        for i in range(left, n):
            nums[i] = 0


s = Solution()
arr = [0, 1, 0, 3, 12]
print(s.moveZeroes(arr))
print(arr)

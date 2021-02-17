'''

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

'''
from typing import List
'''
解题思路：二分查找后向前后搜索
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        index = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if index < 0:
            return [-1, -1]
        left, right = index, index
        while left > 0:
            if nums[left - 1] == target:
                left -= 1
            else:
                break
        while right < len(nums) - 1:
            if nums[right + 1] == target:
                right += 1
            else:
                break
        return [left, right]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([], 0))

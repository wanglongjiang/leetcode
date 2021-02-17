'''
搜索旋转排序数组

升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。

请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

'''

from typing import List
'''
解题思路：二分查找
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] > nums[end] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] > nums[start] or target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 8, 1, 2, 3], 8))
print(s.search([5, 1, 3], 3))
print(s.search([1, 3], 3))
print(s.search([5, 1, 3], 5))
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([1], 0))
print(s.search([3, 1], 1))

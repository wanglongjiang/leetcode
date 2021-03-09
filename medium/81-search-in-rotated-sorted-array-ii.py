'''
搜索旋转排序数组 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
'''
from typing import List
'''
思路：暴力搜索， 官方的二分搜索在最坏情况下是O(n)
'''


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for n in nums:
            if n == target:
                return True
        return False

    def search1(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
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
        return False


s = Solution()
print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(s.search(nums=[1], target=0))

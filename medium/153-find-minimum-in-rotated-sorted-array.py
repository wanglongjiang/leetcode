'''
寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。

请找出其中最小的元素。

提示：

1 <= nums.length <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数都是 唯一 的
nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转
'''
from typing import List
'''
思路：二分查找。
1、小于7的数组，直接遍历。
2、大于7的数组，对比mid与left，right。
    如果mid大于left说明最小值在后半区，继续折半查找后半区。
    如果mid小于left，说明最小值在前半区，继续折半查找前半区。
时间复杂度：O(logn)
空间复杂度：O(1)
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left <= right:
            if right - left < 7:  # 少于7个，直接遍历
                ans = nums[left]
                for i in range(left + 1, right):
                    ans = min(ans, nums[i])
                return ans
            mid = (left + right) // 2  # 折半查找
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid + 1


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([1]))
print(s.findMin([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 1, 2]))

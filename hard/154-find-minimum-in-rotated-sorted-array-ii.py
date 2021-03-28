'''
寻找旋转排序数组中的最小值 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

说明：
这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
'''
from typing import List
'''
思路：折半查找。重复元素会影响算法复杂度。
如果mid>left，最小元素肯定在后半区(不含mid)
如果mid<left，最小元素肯定在前半区（含mid)
如果mid=left，还需要比较mid与right
    如果mid>right，最小元素肯定在后半区
    如果mid<right，这种情况不存在。
    如果mid=right，需要在2个区都查找，如果其中一个区最小值为mid，肯定在另外一个区；如果其中一个区小于mid，不需要查找了，就是这个值。
时间复杂度：>O(logn)
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binSearch(left, right):
            if right - left < 7:  # 小于7，直接查找，速度更快
                ans = nums[left]
                for i in range(left + 1, right):
                    ans = min(ans, nums[i])
                return ans
            mid = (right + left) // 2
            if nums[mid] > nums[left]:  # 如果mid>left，最小元素肯定在后半区(不含mid)
                return binSearch(mid + 1, right)
            if nums[mid] < nums[left]:  # 如果mid<left，最小元素肯定在前半区（含mid)
                return binSearch(left, mid + 1)
            if nums[mid] > nums[right]:  # 如果mid=left，且mid>right，最小元素肯定在后半区
                return binSearch(mid + 1, right)
            ans = binSearch(left, mid)  # 如果mid =left，且mid=right，先查找前半区。备注：mid=left 且 mid<right，这种情况不存在。
            if ans < nums[mid]:  # 如果前半期<mid，肯定就是这个值了
                return ans
            return binSearch(mid + 1, right)  # 前半期有可能=mid，最小值在后半区

        return binSearch(0, len(nums))


s = Solution()
print(s.findMin([1, 3, 5]))
print(s.findMin([2, 2, 2, 0, 1]))

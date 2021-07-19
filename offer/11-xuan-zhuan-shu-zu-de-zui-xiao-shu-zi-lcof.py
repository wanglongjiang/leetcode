'''
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''
from typing import List
'''
思路：二分查找。重复元素会影响算法复杂度。
如果mid>left，且如果mid<= right,最小元素就是第1个，否则最小元素肯定在后半区(不含mid)
如果mid<left，最小元素肯定在前半区（含mid)
如果mid=left，还需要比较mid与right
    如果mid>right，最小元素肯定在后半区
    如果mid<right，这种情况不存在。
    如果mid=right，需要在2个区都查找，如果其中一个区最小值为mid，肯定在另外一个区；如果其中一个区小于mid，不需要查找了，就是这个值。
时间复杂度：>O(logn)
'''


class Solution:
    def minArray(self, nums: List[int]) -> int:
        def binSearch(left, right):
            if right - left < 7:  # 小于7，直接查找，速度更快
                ans = nums[left]
                for i in range(left + 1, right):
                    ans = min(ans, nums[i])
                return ans
            mid = (right + left) // 2
            if nums[mid] > nums[left]:  # 如果mid>left
                if nums[mid] <= nums[right - 1]:  # 如果mid<= right,最小元素就是第1个
                    return nums[left]  # binSearch(left, mid)
                return binSearch(mid + 1, right)  # 如果mid> right,最小元素肯定在后半区(不含mid)
            if nums[mid] < nums[left]:  # 如果mid<left，最小元素肯定在前半区（含mid)
                return binSearch(left, mid + 1)
            if nums[mid] > nums[right - 1]:  # 如果mid=left，且mid>right，最小元素肯定在后半区
                return binSearch(mid + 1, right)
            ans = binSearch(left, mid)  # 如果mid =left，且mid=right，先查找前半区。备注：mid=left 且 mid<right，这种情况不存在。
            if ans < nums[mid]:  # 如果前半期<mid，肯定就是这个值了
                return ans
            return binSearch(mid + 1, right)  # 前半期有可能=mid，最小值在后半区

        return binSearch(0, len(nums))

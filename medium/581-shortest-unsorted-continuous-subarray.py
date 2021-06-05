'''
最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。
提示：

1 <= nums.length <= 10^4
-105 <= nums[i] <= 10^5
'''
from typing import List
'''
思路：双指针
首先从左到右遍历，直至遇到不是升序的左边界left
然后从右到左遍历，直至遇到不是降序的右边界right
在left..right中寻找最大值mx,最小值mi
在0..left中寻找最小值mi应该插入的坐标start
在right..n中寻找最大值mx应该扎入的坐标end
start..end即为应该排序的子数组
时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        while left < n and nums[left] >= nums[left - 1]:  # 跳过升序部分，直至找到1个降序的坐标
            left += 1
        if left == n:  # 如果一直都是升序，没有无序子数组
            return 0
        right = n - 2
        while right > left and nums[right] <= nums[right + 1] and nums[right] >= nums[left - 1]:  # 跳过降序部分，同时需要确保right右边的所有元素要大于left左边的元素
            right -= 1
        mi, mx = float('inf'), float('-inf')
        for i in range(left, right + 1):
            mi = min(mi, nums[i])
            mx = max(mx, nums[i])
        left -= 1
        while left >= 0 and nums[left] > mi:  # 向左找到mi应该在的坐标
            left -= 1
        right += 1
        while right < n and nums[right] < mx:  # 向右找到mx应该在的坐标
            right += 1
        return right - left - 1


s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray([1, 2, 3, 4]))
print(s.findUnsortedSubarray([1]))

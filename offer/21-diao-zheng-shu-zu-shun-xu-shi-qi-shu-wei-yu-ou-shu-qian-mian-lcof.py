'''
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

0 <= nums.length <= 50000
1 <= nums[i] <= 10000
'''
from typing import List
'''
思路：双指针
设2个指针left,right分别指向数组两端
1. left指针向左移动，直至遇到偶数，停止
2. right指针向右移动，直至遇到奇数，停止
3. 交换2个指针指向的值，然后回到1.继续执行，直至left>=right

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2:
                left += 1
            while left < right and nums[right] % 2 == 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return nums

'''
剑指 Offer 57. 和为s的两个数字

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
'''
from typing import List
'''
思路：双指针
设置left,right指针，分别指向数组2端，然后进行如下迭代过程：
> 如果nums[left]+nums[right]>target，right指针向左移动，以减少和
> 如果nums[left]+nums[right]<target,left指针向右移动，以增加和
> 如果nums[left]+nums[right]=target，则返回值

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [nums[left], nums[right]]
        return []

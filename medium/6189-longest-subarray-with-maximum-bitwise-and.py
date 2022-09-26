'''
6189. 按位与最大的最长子数组
给你一个长度为 n 的整数数组 nums 。

考虑 nums 中进行 按位与（bitwise AND）运算得到的值 最大 的 非空 子数组。

换句话说，令 k 是 nums 任意 子数组执行按位与运算所能得到的最大值。那么，只需要考虑那些执行一次按位与运算后等于 k 的子数组。
返回满足要求的 最长 子数组的长度。

数组的按位与就是对数组中的所有数字进行按位与运算。

子数组 是数组中的一个连续元素序列。

 

示例 1：

输入：nums = [1,2,3,3,2,2]
输出：2
解释：
子数组按位与运算的最大值是 3 。
能得到此结果的最长子数组是 [3,3]，所以返回 2 。
示例 2：

输入：nums = [1,2,3,4]
输出：1
解释：
子数组按位与运算的最大值是 4 。 
能得到此结果的最长子数组是 [4]，所以返回 1 。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 106
'''
from typing import List
'''
思路：贪心
子数组按位与最大值即为数组中最大值，题目就是找到最长的全部为最大值的子数组

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num = max(nums)
        ans, i, n = 0, 0, len(nums)
        while i < n:
            while i < n and nums[i] != num:
                i += 1
            start = i
            while i < n and nums[i] == num:
                i += 1
            ans = max(ans, i - start)
        return ans


s = Solution()
print(s.longestSubarray([1, 2, 3, 3, 2, 2]))
print(s.longestSubarray([1, 2, 3, 4]))

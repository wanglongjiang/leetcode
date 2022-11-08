'''
2461. 长度为 K 子数组中的最大和
中等
15
相关企业
给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：

子数组的长度是 k，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。

子数组 是数组中一段连续非空的元素序列。

 

示例 1：

输入：nums = [1,5,4,2,9,9,9], k = 3
输出：15
解释：nums 中长度为 3 的子数组是：
- [1,5,4] 满足全部条件，和为 10 。
- [5,4,2] 满足全部条件，和为 11 。
- [4,2,9] 满足全部条件，和为 15 。
- [2,9,9] 不满足全部条件，因为元素 9 出现重复。
- [9,9,9] 不满足全部条件，因为元素 9 出现重复。
因为 15 是满足全部条件的所有子数组中的最大子数组和，所以返回 15 。
示例 2：

输入：nums = [4,4,4], k = 3
输出：0
解释：nums 中长度为 3 的子数组是：
- [4,4,4] 不满足全部条件，因为元素 4 出现重复。
因为不存在满足全部条件的子数组，所以返回 0 。
 

提示：

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
'''
from collections import Counter
from typing import List
'''
[TOC]

# 思路
滑动窗口

# 解题方法
> 设一个大小为k的滑动窗口，滑过数组nums
> 滑动过程中，用一个哈希表对窗口中的元素进行计数，如果没有重复元素，将其和尝试记录到结果中

# 复杂度
- 时间复杂度: 
>  $O(k)$

- 空间复杂度: 
> $O(k)$
'''


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s, counter = sum(nums[:k]), Counter(nums[:k])
        ans = s if len(counter) == k else 0
        for i in range(k, len(nums)):
            s -= nums[i - k]
            counter[nums[i - k]] -= 1
            if counter[nums[i - k]] == 0:
                del counter[nums[i - k]]
            s += nums[i]
            counter[nums[i]] += 1
            if len(counter) == k:
                ans = max(ans, s)
        return ans


s = Solution()
assert s.maximumSubarraySum(nums=[4, 4, 4], k=3) == 0
assert s.maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3) == 15

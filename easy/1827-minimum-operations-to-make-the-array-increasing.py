'''
1827. 最少操作使数组递增
简单
32
相关企业
给你一个整数数组 nums （下标从 0 开始）。每一次操作中，你可以选择数组中一个元素，并将它增加 1 。

比方说，如果 nums = [1,2,3] ，你可以选择增加 nums[1] 得到 nums = [1,3,3] 。
请你返回使 nums 严格递增 的 最少 操作次数。

我们称数组 nums 是 严格递增的 ，当它满足对于所有的 0 <= i < nums.length - 1 都有 nums[i] < nums[i+1] 。一个长度为 1 的数组是严格递增的一种特殊情况。

 

示例 1：

输入：nums = [1,1,1]
输出：3
解释：你可以进行如下操作：
1) 增加 nums[2] ，数组变为 [1,1,2] 。
2) 增加 nums[1] ，数组变为 [1,2,2] 。
3) 增加 nums[2] ，数组变为 [1,2,3] 。
示例 2：

输入：nums = [1,5,2,4,1]
输出：14
示例 3：

输入：nums = [8]
输出：0
 

提示：

1 <= nums.length <= 5000
1 <= nums[i] <= 104
'''
from typing import List
'''
[TOC]

# 思路
一次遍历

# 解题方法

依次遍历每个元素，如果当前元素nums[i]<=nums[i-1]，需要将nums[i]增加nums[i-1]-nums[i]+1

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev >= nums[i]:
                ans += prev - nums[i] + 1
                prev += 1
            else:
                prev = nums[i]
        return ans


s = Solution()
assert s.minOperations(nums=[1, 5, 2, 4, 1]) == 14

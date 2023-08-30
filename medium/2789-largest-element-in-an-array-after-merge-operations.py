from typing import List
'''
[TOC]

# 思路
贪心

# 解题方法
从右向左遍历数组，遇到nums[i+1]>=nums[i]，向左累计求和，直至遇到不满足条件

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        s = 0
        for num in reversed(nums):
            if s >= num:
                s += num
            else:
                s = num
        return s

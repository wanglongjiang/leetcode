'''
805. 数组的均值分割
困难
127
相关企业
给定你一个整数数组 nums

我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) == average(B) 。

如果可以完成则返回true ， 否则返回 false  。

注意：对于数组 arr ,  average(arr) 是 arr 的所有元素除以 arr 长度的和。

 

示例 1:

输入: nums = [1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
示例 2:

输入: nums = [3,1]
输出: false
 

提示:

1 <= nums.length <= 30
0 <= nums[i] <= 104
'''
from typing import List
'''
[TOC]

# 思路
动态规划

# 解题方法


# 复杂度
- 时间复杂度: 
> $O(k^n)$

- 空间复杂度: 
> $O(k^n)$
'''


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        m = n // 2
        s = sum(nums)
        if all(s * i % n for i in range(1, m + 1)):
            return False

        dp = [set() for _ in range(m + 1)]
        dp[0].add(0)
        for num in nums:
            for i in range(m, 0, -1):
                for x in dp[i - 1]:
                    curr = x + num
                    if curr * n == s * i:
                        return True
                    dp[i].add(curr)
        return False

'''
2501. 数组中最长的方波
中等
4
相关企业
给你一个整数数组 nums 。如果 nums 的子序列满足下述条件，则认为该子序列是一个 方波 ：

子序列的长度至少为 2 ，并且
将子序列从小到大排序 之后 ，除第一个元素外，每个元素都是前一个元素的 平方 。
返回 nums 中 最长方波 的长度，如果不存在 方波 则返回 -1 。

子序列 也是一个数组，可以由另一个数组删除一些或不删除元素且不改变剩余元素的顺序得到。

 

示例 1 ：

输入：nums = [4,3,6,16,8,2]
输出：3
解释：选出子序列 [4,16,2] 。排序后，得到 [2,4,16] 。
- 4 = 2 * 2.
- 16 = 4 * 4.
因此，[4,16,2] 是一个方波.
可以证明长度为 4 的子序列都不是方波。
示例 2 ：

输入：nums = [2,3,5,6,7]
输出：-1
解释：nums 不存在方波，所以返回 -1 。
 

提示：

2 <= nums.length <= 105
2 <= nums[i] <= 105
'''
from typing import List
'''
[TOC]

# 思路
排序 哈希表

# 解题方法
1. 将nums从大到小排序
2. 设一个哈希表，用于保存nums中的元素
3. 遍历nums，如果当前元素nums[i]的平方在哈希表中存在，则将该序列的长度+1

# 复杂度
- 时间复杂度: 
> $O(nlogn)$ 

- 空间复杂度: 
> $O(n)$
'''


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        seqLen = {}
        ans = -1
        for num in nums:
            pre = num * num
            if pre in seqLen:
                if num not in seqLen:
                    seqLen[num] = seqLen[pre] + 1
                    ans = max(ans, seqLen[num])
            else:
                seqLen[num] = 1
        return ans

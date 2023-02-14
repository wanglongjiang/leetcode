'''
2563. 统计公平数对的数目
中等
19
相关企业
给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。

如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：

0 <= i < j < n，且
lower <= nums[i] + nums[j] <= upper
 

示例 1：

输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6
输出：6
解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
示例 2：

输入：nums = [1,7,9,2,5], lower = 11, upper = 11
输出：1
解释：只有单个公平数对：(2,3) 。
 

提示：

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
'''
from typing import List
import bisect
'''
[TOC]

# 思路
排序 二分查找

# 解题方法
1. nums排序
2. 遍历nums中的每个元素num，用二分查找查找lower-num和upper-num，找到的子数组中的元素全都可以与num构成公平数对


# 复杂度
- 时间复杂度: 
> $O(nlogn)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            left = bisect.bisect_left(nums, lower - num)
            if left > len(nums):
                continue
            right = bisect.bisect_right(nums, upper - num)
            if right <= left:
                continue
            ans += right - left
            if left <= i < right:
                ans -= 1
        return ans // 2


s = Solution()
assert s.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6) == 6
assert s.countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11) == 1

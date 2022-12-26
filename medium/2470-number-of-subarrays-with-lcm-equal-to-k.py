'''
2470. 最小公倍数为 K 的子数组数目
中等
12
相关企业
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的 子数组 中满足 元素最小公倍数为 k 的子数组数目。

子数组 是数组中一个连续非空的元素序列。

数组的最小公倍数 是可被所有数组元素整除的最小正整数。

 

示例 1 ：

输入：nums = [3,6,2,7,1], k = 6
输出：4
解释：以 6 为最小公倍数的子数组是：
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
示例 2 ：

输入：nums = [3], k = 2
输出：0
解释：不存在以 2 为最小公倍数的子数组。
 

提示：

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000
'''
from math import lcm
from typing import List
'''
[TOC]

# 思路
动态规划

# 解题方法
设数组dp[n][n]，dp[i][j]的意思是子数组nums[i..j]的最小公倍数，状态转移方程为：
> dp[i][j] = lcm(dp[i][j-1],nums[j])

可以用一个2重循环遍历所有的状态进行计算。

当d[i][j]>k时，可以终止循环，优化时间
另外，因为状态只依赖于上一个，还可以进行空间优化


# 复杂度
- 时间复杂度: 
> $O(n^{2})$

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            dp = nums[i]
            for j in range(i, n):
                dp = lcm(dp, nums[j])
                if dp == k:
                    ans += 1
                elif dp > k:
                    break
        return ans


s = Solution()
assert s.subarrayLCM(nums=[3, 6, 2, 7, 1], k=6) == 4
assert s.subarrayLCM(nums=[3], k=2) == 0

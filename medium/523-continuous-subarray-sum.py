'''
连续的子数组和
给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。

 

示例 1：

输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
示例 2：

输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
示例 3：

输入：nums = [23,2,6,4,7], k = 13
输出：false
 

提示：

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
'''
from typing import List
'''
思路：哈希+数学
直接暴力求各个子数组的和然后除以k来搜索，时间复杂度为O(n^2)，会超时。
继续一步思考，求数组的和是k的整数倍，如果数组的和sum%k==0，满足要求，如果sum%k==a，如果在数组的子数组里面找到subsum%k==a，
这种情况下sum-subsum肯定是k的整数倍
根据上面的思路写出算法：
遍历nums，用prefixSum保存前缀和，然后设r=prefixSum%k，再设一个哈希集合rset保存r
> 如果r为0则满足要求;
> 如果r不为0，查找之前的前缀和除以k的余数(已保存到rset中）是否有r存在，如果存在，说明有子数组的和为k的整数倍

时间复杂度：O(n)，只遍历一次数组
空间复杂度：O(n)，需要用哈希表保存余数
'''


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        rset, prefixSum, prer = set(), nums[0], nums[0] % k
        for i in range(1, len(nums)):
            prefixSum += nums[i]  # 求和
            r = prefixSum % k
            if r == 0:  # 余数如果为0，满足要求
                return True
            elif r in rset:  # 余数如果在之前的子数组和余数集合中存在，满足要求
                return True
            rset.add(prer)  # 将前一个数组的余数加入集合，目的是只能在隔一个元素之前的余数集合里面查找，防止出现大小为1的子数组
            prer = r
        return False


s = Solution()
print(not s.checkSubarraySum([1, 0], 2))
print(s.checkSubarraySum([1, 2, 3], 5))
print(s.checkSubarraySum([1, 1], 1))
print(not s.checkSubarraySum([0, 1, 0, 3, 0, 4, 0, 4, 0], 5))
print(not s.checkSubarraySum([1, 2, 12], 6))
print(s.checkSubarraySum([5, 0, 0, 0], 3))
print(s.checkSubarraySum([0, 0], 2))
print(s.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
print(s.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
print(not s.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))

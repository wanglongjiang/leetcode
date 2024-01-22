from typing import List
'''
[TOC]

# 思路
排序 贪心 前缀和

# 解题方法
根据题意得知，最长边不能超过剩下的边之和，所以从大往小依次尝试将其设置为最长边，如果可以，则即为最大周长
详细方法见代码及注释

# 复杂度
- 时间复杂度: 
> $O(n*log(n))$ ，对数组进行排序，时间复杂度为nlog(n)

- 空间复杂度: 
> $O(1)$
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefixSum = sum(nums) - nums[-1]  # 前缀和
        i = len(nums) - 1  # 当前最长边长
        while prefixSum <= nums[i] and i > 1: # 如果前缀和小于等于最长边，该最长边不满足要求，需要换一个更短的
            i -= 1
            prefixSum -= nums[i]
        if i > 1: # 至少是三条边才满足要求
            return prefixSum + nums[i]
        return -1

s=Solution()
assert s.largestPerimeter([1,12,1,2,5,50,3])==12

    
'''
462. 最少移动次数使数组元素相等 II
给你一个长度为 n 的整数数组 nums ，返回使所有数组元素相等需要的最少移动数。

在一步操作中，你可以使数组中的一个元素加 1 或者减 1 。

 

示例 1：

输入：nums = [1,2,3]
输出：2
解释：
只需要两步操作（每步操作指南使一个元素加 1 或减 1）：
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
示例 2：

输入：nums = [1,10,2,9]
输出：16
 

提示：

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

from typing import List
'''
思路：数学 排序 前缀和
先对数组进行排序
如果整个数组变成元素nums[i]，整个数组需要操作的次数就是nums[i]*i-sum(nums[0:i]) + sum(nums[i+1:n])-nums[i]*(n-i-1)
遍历整个数组，找到操作次数最小的那个。

时间复杂度：O(n)
空间复杂度：O(1)
'''


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        # 计算前缀和，方便计算sum(nums[:i])等
        prefixSum, n = [0] * len(nums), len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        # 特殊处理第0个元素
        ans = abs(prefixSum[-1] - nums[0] * n)
        # 特殊处理最后一个元素
        ans = min(ans, abs(nums[-1] * n - prefixSum[-1]))
        # 迭代处理剩余的元素
        for i in range(1, n - 1):
            ans = min(ans, nums[i] * i - prefixSum[i - 1] + prefixSum[-1] - prefixSum[i] - nums[i] * (n - i - 1))
        return ans

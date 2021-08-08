'''
旋转函数
给定一个长度为 n 的整数数组 A 。

假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算F(0), F(1), ..., F(n-1)中的最大值。

注意:
可以认为 n 的值小于 10^5。

示例:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
'''
from typing import List
'''
思路：数学 前缀数组 动态规划
1. 求数组前缀和
2. f(0)=nums[0]*0+nums[1]*1..+nums[n-1]*(n-1)
状态转移方程为：
f(i)=f(i-1)-prefixSum[i-2]+nums[i-1]*(n-1)-nums[i]-(prefixSum[n-1]-prefixSum[i])
意思是f(i)与f(i-1)相比，发生了1个元素的旋转，
变成0的是nums[i]的乘积，原先nums[i-1]由0变成nums[i-1]*(n-1)，其他每个元素的乘数会减一（使用前缀和数组实现）

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]  # 计算前缀和
        dp = [0] * n
        for i, num in enumerate(nums):  #
            dp[0] += i * num  # 计算旋转次数为0时的结果
        for i in range(1, n):
            dp[i] = dp[i - 1] - (prefixSum[i - 2] if i > 1 else 0) + nums[i - 1] * (n - 1) - nums[i] - (prefixSum[n - 1] - prefixSum[i])
        return max(dp)


s = Solution()
print(s.maxRotateFunction([4, 3, 2, 6]))

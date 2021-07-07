'''
最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
'''
from typing import List
'''
思路1，贪心算法
用一个变量pre保存nums[i-1]之前的子数组和，
> 如果pre>0，则截止nums[i]的最大子数组和为pre+nums[i]
> 如果pre<=0，则截止nums[i]的最大子数组和为nums[i]

时间复杂度：O(n)
空间复杂度：O(1)

思路2，动态规划
设dp[i]为截止第i个元素，连续最大子数组和
dp[i] = max(dp[i-1]+nums[i], nums[i])

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    def maxSubArray1(self, nums: List[int]) -> int:
        pre = 0
        maxSum = nums[0]
        for num in nums:
            pre = max(pre + num, num)
            maxSum = max(maxSum, pre)
        return maxSum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(s.maxSubArray([1]) == 1)
print(s.maxSubArray([0]) == 0)
print(s.maxSubArray([-100000]) == -100000)

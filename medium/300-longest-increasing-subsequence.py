'''
最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
提示：

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
 

进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''
from typing import List
'''
思路：动态规划
设二维数组dp[n][n]，dp[i][j]的含义为：i<j，以第i个元素开头的序列，遍历到第j个元素子序列的长度
状态转移方程为：
if nums[j]>nums[j-1]
    dp[i][j]=max(dp[i][j-1]+1,dp[i-1][j-1]+1)
else
    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
时间复杂度：O(n^2)
空间复杂度：O(n^2)
TODO
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1] * (n + 1) for _ in range(n + 1)]  # 默认长度是1，为简化算法，下标0作为哨兵
        for i in range(1, n + 1):
            dp[i][i] = dp[i - 1][i]
            for j in range(i + 1, n + 1):
                if nums[j - 1] > nums[j - 2]:
                    dp[i][j] = max(dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i - 1][0], dp[i - 1][j])
        return dp[n - 1][n]


s = Solution()
print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))

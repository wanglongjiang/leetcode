'''
1262. 可被三整除的最大和
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。

 

示例 1：

输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
示例 2：

输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。
示例 3：

输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
 

提示：

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
'''
from typing import List
'''
思路：动态规划


'''


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(nums) + 1)]
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                dp[i + 1][0] = max(dp[i][0], dp[i][0] + nums[i])
                dp[i + 1][1] = max(dp[i][1], dp[i][1] + nums[i])
                dp[i + 1][2] = max(dp[i][2], dp[i][2] + nums[i])
            elif nums[i] % 3 == 1:
                dp[i + 1][0] = max(dp[i][0], dp[i][2] + nums[i])
                dp[i + 1][1] = max(dp[i][1], dp[i][0] + nums[i])
                dp[i + 1][2] = max(dp[i][2], dp[i][1] + nums[i])
            else:
                dp[i + 1][0] = max(dp[i][0], dp[i][1] + nums[i])
                dp[i + 1][1] = max(dp[i][1], dp[i][2] + nums[i])
                dp[i + 1][2] = max(dp[i][2], dp[i][0] + nums[i])
        return dp[-1][0]


s = Solution()
print(s.maxSumDivThree([3, 6, 5, 1, 8]))

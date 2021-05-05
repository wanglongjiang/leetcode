'''
删除并获得点数

给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

 

示例 1：

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
示例 2：

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
 

提示：

1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4
'''
from typing import List
'''
思路，动态规划
因nums[i]最大是10^4，可以设一个最长为10^4+1的dp数组，每个元素代表截止数字i能获得的最大点数
状态转移方程为：dp[i] = max(数字i的累计和+dp[i-2], dp[i-1])
状态转移方程的含义是：
    a、如果选择了当前数字，当前数字的累计和可以与隔1个数字的dp[i-2]相加；
    b、如果不选择当前数字，dp[i]与dp[i-1]相同
    在上面a、b两者选择较大的一个
i=0,dp[0]=0
i=1,dp[1]=1的累计数
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxnum = max(nums)
        sums = [0] * (maxnum + 1)  # 累计各个数字的和
        for num in nums:
            sums[num] += num
        dp = [0] * (maxnum + 1)  # 动态规划数组，存放截止数字i为止的最大点数
        dp[1] = sums[1]
        for i in range(2, maxnum + 1):
            dp[i] = max(sums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]


s = Solution()
print(s.deleteAndEarn([3, 4, 2]))
print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))

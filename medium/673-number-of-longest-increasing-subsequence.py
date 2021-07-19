'''
最长递增子序列的个数

给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
'''
from typing import List
'''
思路：动态规划
与通常的求LIS略有不同。这里是求最长递增子序列的个数，因此需要记录计算所有的最长子序列。
使用动态规划算法，设dp[n]初始为1，对于dp[i]意思是截止nums[i]，最长子序列的长度。
dp[i] = max(dp[0..i-1])+1，如果dp[0..i-1]中有多个，需要对个数进行累计

时间复杂度：O(n^2)
空间复杂度：O(n)
'''


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxLen, ans = 1, 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > maxLen:
                        maxLen = dp[i]
                        ans = 1
                    elif dp[i] == maxLen:
                        ans += 1
        if maxLen == 1:  # 如果最大递增子序列长度为1，也就是数组所有元素相同或者为递减序列，子序列个数为数组长度
            ans = n
        return ans


s = Solution()
print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
print(s.findNumberOfLIS([2, 2, 2, 2, 2]))

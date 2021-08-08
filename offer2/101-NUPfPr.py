'''
剑指 Offer II 101. 分割等和子串
给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。

 

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：nums 可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：nums 不可以分为和相等的两部分
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
 

注意：本题与主站 416 题相同： https://leetcode-cn.com/problems/partition-equal-subset-sum/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/NUPfPr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
思路1，暴力组合
组合公式为n!/m!(n-m)!，会超时

思路2，动态规划
0-1背包问题的变形，设置一个二维数组dp[i][j]，含义是第i个数字选择与否，是否能使和为j
0<=i<=n, 0<=j<=sum(nums)/2
状态转移方程为：
dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
含义是如果减掉当前整数nums[i-1]后，前i-1个整数的组合正好满足和的要求（j-nums[i-1]），则为true
否则可以不选当前整数，从上一个整数的组合继承dp[i-1][j]
初始化：dp[0][..]都是false，表示如果不选择任何整数，为False
dp[..][0]都是true,表示任何整数都不选，其和就是0
dp数组大小为dp[N][total]，N = len(total)+1, sums = sum(total)/2+1
'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:  # 少于2个，不能切分
            return False
        total = sum(nums)
        if total % 2 == 1:  # 和为奇数，肯定无法平均分成2份
            return False
        total //= 2
        dp = [[False] * (total + 1) for _ in range(n + 1)]  # 初始化
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, total + 1):
                if j - nums[i - 1] < 0:  # 当前整数超过j，肯定不能选择，从上一个组合继承
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
            if dp[i][total]:
                return True
        return dp[n][total]


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))

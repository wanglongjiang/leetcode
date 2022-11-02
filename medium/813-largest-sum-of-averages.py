'''
813. 最大平均值和的分组
给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。

注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。

返回我们所能得到的最大 分数 是多少。答案误差在 10-6 内被视为是正确的。

 

示例 1:

输入: nums = [9,1,2,3,9], k = 3
输出: 20.00000
解释: 
nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20. 
我们也可以把 nums 分成[9, 1], [2], [3, 9]. 
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
示例 2:

输入: nums = [1,2,3,4,5,6,7], k = 4
输出: 20.50000
 

提示:

1 <= nums.length <= 100
1 <= nums[i] <= 104
1 <= k <= nums.length
'''
import itertools
from typing import List
'''
思路：
设3维数组dp，dp[i][j]的意思是第i个子数组，截止下标为j时的分数。
那么状态转移方程为：dp[i][j]=max(dp[i-1][x-1]+average(nums[x..j]))，其中x取值范围为i..j，是第i个子数组与第i-1个子数组的分割点

时间复杂度：O(n^3)
空间复杂度：O(n^2)
'''


class Solution:

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(k)]
        # 计算前缀和
        prefixsum = [0]
        prefixsum.extend((itertools.accumulate(nums)))
        # 初始化
        for j in range(1, n - k + 2):
            dp[0][j] = prefixsum[j] / j
        # 开始动态规划
        for i in range(1, k):
            for j in range(i, n - (k - i) + 2):
                for x in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][x - 1] + (prefixsum[j] - prefixsum[x - 1]) / (j - x + 1))
        return max(dp[-1])


s = Solution()
assert s.largestSumOfAverages([4, 1, 7, 5, 6, 2, 3], 4) == 18.16667  # TODO
print(s.largestSumOfAverages(nums=[9, 1, 2, 3, 9], k=3))
print(s.largestSumOfAverages(nums=[1, 2, 3, 4, 5, 6, 7], k=4))

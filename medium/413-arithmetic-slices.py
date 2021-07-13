'''
等差数列划分

如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。
'''
from typing import List
'''
思路：动态规划
当nums[i]-nums[i-1]==nums[i-1]-nums[i-2]时为等差序列
dp[i]=1+dp[i-1]

时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = 1 + dp[i - 1]
        return sum(dp)


s = Solution()
print(s.numberOfArithmeticSlices([1, 2, 3, 4, 6, 8, 10]))
print(s.numberOfArithmeticSlices([1, 2, 3, 4]))
print(s.numberOfArithmeticSlices([1, 2, 3]))

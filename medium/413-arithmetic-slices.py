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
思路：等差数列+数学
首先计算出数组的等差数组，然后统计连续相同的数字个数m
对于m>=3,需要计算其子数组个数
m=3，count=1
m=4,count=(m-3)+1 + m-4+1
m=5,count=(m-3)+1 + (m-4)+1 + (m-5)+1
时间复杂度：O(n)
空间复杂度：O(n)
'''


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * n
        for i in range(1, n):  # 计算等差数组
            diff[i] = nums[i] - nums[i - 1]
        diff[0] = float('-inf')
        diffLens = []
        pre = float('inf')
        dcount = 0
        for d in diff:  # 分析等差数组，将等差数组的长度保存到diffLens
            if d == pre:
                dcount += 1
            else:
                pre = d
                if dcount >= 2:
                    diffLens.append(dcount + 1)
                dcount = 1
        if dcount >= 3:
            diffLens.append(dcount + 1)
        # 对于每个等差数组，计算其子数组的数量
        count = 0
        for m in diffLens:
            for k in range(3, m + 1):
                count += m - k + 1
        return count


s = Solution()
print(s.numberOfArithmeticSlices([1, 2, 3, 4, 6, 8, 10]))
print(s.numberOfArithmeticSlices([1, 2, 3, 4]))

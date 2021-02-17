'''
数组拆分 I
给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。

返回该 最大总和 。
'''

from typing import List
'''
思路：要想使和最大，需要使2个序列的差最小。方法是对数组进行排序，每次选出相邻的2个元素组成1对
求min的和，可以从下标0开始，偶数下标求和
'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans


s = Solution()
print(s.arrayPairSum([1, 4, 3, 2]))
print(s.arrayPairSum([6, 2, 6, 5, 1, 2]))

'''
分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

1 <= nums.length <= 200
1 <= nums[i] <= 100

'''
from typing import List
'''
思路1，暴力组合
组合公式为n!/m!(n-m)!，会超时

思路2，回溯
求数组所有元素和total，可以将问题转化为从nums中选取任意元素，使其和为total/2
时间也很长啊
TODO
'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))

'''
划分为k个相等的子集

给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
提示：

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000
'''
from functools import cache
from typing import List
'''
思路：回溯+记忆化搜索
首先判断数组之和total/k能被整除，如果不能整除，则没有解
然后商d为每个子数组之和，nums中最大元素如果大于d，则没有解
如果通过了上面的检查，每次从数组中选取x个数组成子集，如果子集的等于d，进入下一层，如果找不到等于d的子集，返回false

时间复杂度：O(2^n*n)，组合有2^n种，再加上每层查找的过程
空间复杂度：O(n)
'''


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        @cache
        def dfs(state, summ):

            if state == (1 << n) - 1:  # 所有整数均已划分，结束递归，并返回True
                return True

            for j in range(n):
                if summ + nums[j] > target:  # nums已升序排列，当前数字不行，后续肯定也不行
                    break
                if state & (1 << j) == 0:  # nums[i]暂未被划分
                    next_state = state + (1 << j)  # 划分nums[i]
                    if dfs(next_state, (summ + nums[j]) % target):  # 划分nums[i]能形成有效方案
                        return True
            return False

        total = sum(nums)
        if total % k != 0:
            return False
        n = len(nums)
        target = total // k  # 目标非空子集的和
        nums.sort()  # 升序排列
        if nums[-1] > target:  # 最大值超过目标子集和，无法划分
            return False
        return dfs(0, 0)


s = Solution()
print(s.canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5], 4))
print(s.canPartitionKSubsets([3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10))
print(s.canPartitionKSubsets([129, 17, 74, 57, 1421, 99, 92, 285, 1276, 218, 1588, 215, 369, 117, 153, 22], 3))
print(s.canPartitionKSubsets([10, 12, 1, 2, 10, 7, 5, 19, 13, 1], 4))
print(s.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
print(s.canPartitionKSubsets([1739, 5391, 8247, 236, 5581, 11, 938, 58, 1884, 823, 686, 1760, 6498, 6513, 6316, 2867], 6))

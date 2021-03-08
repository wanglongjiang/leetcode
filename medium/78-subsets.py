'''
子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''
from typing import List
'''
思路：回溯查找所有组合
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        comb = []
        n = len(nums)

        def backtrack(index: int, k: int):
            if len(comb) == k:
                ans.append(comb.copy())
            for i in range(index, n):
                comb.append(nums[i])
                backtrack(i + 1, k)
                comb.pop()

        for i in range(len(nums) + 1):
            backtrack(0, i)
        return ans


s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([0]))

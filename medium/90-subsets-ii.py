'''
子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
'''
from typing import List
'''
思路：回溯所有组合，并跳过重复的子集
与78题类似，不同之处在于输入有重复元素，需要跳过。
跳过的方法是先对输入进行排序，回溯时如果遇到重复元素就跳过
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        comb = []
        n = len(nums)

        def backtrack(index: int, k: int):
            if len(comb) == k:
                ans.append(comb.copy())
            i = index
            while i < n:
                comb.append(nums[i])
                backtrack(i + 1, k)
                comb.pop()
                while i + 1 < n and nums[i] == nums[i + 1]:  # 跳过重复的元素
                    i += 1
                else:
                    i += 1

        for i in range(len(nums) + 1):
            backtrack(0, i)
        return ans


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))

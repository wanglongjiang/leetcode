'''
组合总和 II

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

'''
from typing import List
'''
解题思路：参照上题思路，搜索回溯
'''


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        result = []
        combination = []

        def findCombination(target, index):
            if target == 0:
                result.append(combination.copy())
                return
            if index == len(candidates):
                return
            findCombination(target, index + 1)
            if target - candidates[index] >= 0:
                combination.append(candidates[index])
                findCombination(target - candidates[index], index + 1)
                combination.pop()

        findCombination(target, 0)
        return result


s = Solution()
print(s.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
print(s.combinationSum([2, 5, 2, 1, 2], 5))

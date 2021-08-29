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
回溯搜索
1. 排序
2. 将index指向的数值从target中减掉，使target=target-arr[index]，然后index+1，继续搜索
3. 或者跳过index，从index+1之后继续搜索target
4. 重复上面的2，3回溯搜索过程，将target等于0的所有组合加入list

时间复杂度：O(n!)，因为有剪枝的存在，会远远小于
空间复杂度：O(n)
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 经过排序，下面的回溯可以进行剪枝
        if sum(candidates) < target:
            return []
        result = []
        combination = []

        def findCombination(target, index):
            if target == 0:
                result.append(combination.copy())
                return
            if index == len(candidates):
                return
            if target - candidates[index] >= 0:
                combination.append(candidates[index])
                findCombination(target - candidates[index], index + 1)
                combination.pop()
                while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:  # 剪枝，排除相同的数值、相同的target
                    index += 1
                findCombination(target, index + 1)
            else:
                return

        findCombination(target, 0)
        return result


s = Solution()
print(
    s.combinationSum2([
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    ], 30))
print(s.combinationSum2([2, 5, 2, 1, 2], 5))
print(s.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 9))
print(s.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27))
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

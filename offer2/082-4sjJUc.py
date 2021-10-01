'''
剑指 Offer II 082. 含有重复元素集合的组合
给定一个可能有重复数字的整数数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。 

 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
 

提示:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
 

注意：本题与主站 40 题相同： https://leetcode-cn.com/problems/combination-sum-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sjJUc
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''
解题思路：回溯
参照上题剑指 Offer II 081.[允许重复选择元素的组合](offer2/081-Ygoe9J.py)思路，搜索回溯
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if sum(candidates) < target:
            return []
        result = []
        combination = []
        unionSet = set()

        def findCombination(target, index):
            if target == 0:
                # 利用set排重
                unionId = ','.join(map(str, combination))
                if unionId not in unionSet:
                    result.append(combination.copy())
                    unionSet.add(unionId)
                return
            if index == len(candidates):
                return
            if target - candidates[index] >= 0:
                combination.append(candidates[index])
                findCombination(target - candidates[index], index + 1)
                combination.pop()
            findCombination(target, index + 1)

        findCombination(target, 0)
        return result

'''
组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

'''
from typing import List
'''
解题思路：一个解视为[a,target-a的组合]，a=for a in candidates，递归向下依次查找可能的解
'''


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combination = []
        unionSet = set()

        def findCombination(target):
            for num in candidates:
                if num == target:
                    newcom = combination.copy()
                    newcom.append(num)
                    newcom.sort()
                    unionId = ','.join(map(str, newcom))
                    if unionId not in unionSet:
                        result.append(newcom)
                        unionSet.add(unionId)
                elif num < target:
                    combination.append(num)
                    findCombination(target - num)
                    combination.pop()
                else:
                    return

        findCombination(target)
        return result


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))

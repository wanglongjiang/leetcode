'''
组合总和 III
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
'''
from typing import List
'''
思路：回溯查找所有组合
时间复杂度：O(n!/(m!(n-m!)))，组合
空间复杂度：O(k)，最多递归k层和另外的大小为k的辅助空间
'''


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        comb = []

        def backtrack(index, target):
            remainderNums = k - len(comb) - 1
            if remainderNums == 0 and target < 10:
                copy = comb.copy()
                copy.append(target)
                ans.append(copy)
            else:
                for i in range(index + 1, 10):
                    if target - i > i + remainderNums - 1:  # 当前遍历到的数进入下一过程会更大，另外组合中的数字必须达到k
                        comb.append(i)
                        backtrack(i, target - i)
                        comb.pop()
                    else:  # 不满足上面条件的数，后面的数更不会满足，可以跳出
                        break

        backtrack(0, n)
        return ans


s = Solution()
print(s.combinationSum3(k=3, n=7))
print(s.combinationSum3(k=3, n=9))
print(s.combinationSum3(k=3, n=10))
print(s.combinationSum3(k=2, n=10))
print(s.combinationSum3(k=1, n=6))
print(s.combinationSum3(k=2, n=18))

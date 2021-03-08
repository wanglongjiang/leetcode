'''
组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
'''
from typing import List
'''
思路：回溯组合
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []

        def backtrack(index: int):
            for i in range(index, n + 1):
                comb.append(i)
                if len(comb) == k:
                    ans.append(comb.copy())
                else:
                    backtrack(i + 1)
                comb.pop()

        backtrack(1)
        return ans


s = Solution()
print(s.combine(4, 2))

'''
递增子序列
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是 2 。

 

示例：

输入：[4, 6, 7, 7]
输出：[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 

提示：

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
'''
from typing import List
'''
思路：回溯+剪枝
回溯查找所有可能的组合，组合中有可能有重复数据，用hashset去重。

时间复杂度：O(2^n)
空间复杂度：O(n)
'''


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()  # 用Set去重

        def backtrack(index, seq):
            if not seq or nums[index] >= seq[-1]:  # 剪枝，跳过不能形成递增序列的元素
                seq.append(nums[index])
                if len(seq) > 1:
                    ans.add(tuple(seq))
                if index < n - 1:
                    backtrack(index + 1, seq)
                seq.pop()
            if index < n - 1:
                backtrack(index + 1, seq)

        backtrack(0, [])
        return [list(item) for item in ans]


s = Solution()
print(s.findSubsequences([7, 7, 7]))
print(s.findSubsequences([4, 6, 7, 7]))
print(s.findSubsequences([4, 6, 7, 8]))

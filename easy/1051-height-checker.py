'''
高度检查器
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。

请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。

注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。
'''
from typing import List
'''
思路：原数组复制后排序对比。
排序可以用计数排序，但数组较小，直接用系统内置快排。
'''


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums = heights.copy()
        nums.sort()
        ans = 0
        for i in range(len(heights)):
            if heights[i] != nums[i]:
                ans += 1
        return ans


s = Solution()
print(s.heightChecker([1, 1, 4, 2, 1, 3]))
print(s.heightChecker([5, 1, 2, 3, 4]))
print(s.heightChecker([1, 2, 3, 4, 5]))

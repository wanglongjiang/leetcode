'''
杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
'''
from typing import List
'''
思路：大学课程里面的杨辉三角，怀念
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [None] * numRows
        for i in range(1, numRows + 1):
            ans[i - 1] = [1] * i
            for j in range(1, i - 1):  # 第1个和最后1个都是1，不需要计算
                ans[i - 1][j] = ans[i - 2][j] + ans[i - 2][j - 1]
        return ans


s = Solution()
print(s.generate(1))
print(s.generate(2))
print(s.generate(3))
print(s.generate(4))
print(s.generate(5))

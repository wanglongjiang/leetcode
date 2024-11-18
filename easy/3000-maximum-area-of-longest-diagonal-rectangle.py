'''
[TOC]

# 思路
贪心

# 解题方法
遍历输入数组，找到对角线最长，即平方和最大的一组，返回其面积即可

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # 遍历输入数组，找到对角线最长，即平方和最大的一组，返回其面积即可
        max_len = 0
        max_area = 0
        for dimension in dimensions:
            length = dimension[0]**2 + dimension[1]**2
            if length > max_len:
                max_len = length
                max_area = dimension[0] * dimension[1]
            elif length == max_len:
                max_area = max(max_area, dimension[0] * dimension[1])
        return max_area

assert Solution().areaOfMaxDiagonal([[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]])== 20

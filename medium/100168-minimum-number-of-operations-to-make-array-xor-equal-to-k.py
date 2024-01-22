'''
[TOC]

# 思路
位运算

# 解题方法
题目实际上是求nums中所有元素异或结果，与k异或后的1的个数

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''
from typing import List
from functools import reduce
from operator import xor


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return reduce(xor,nums,k).bit_count()
    
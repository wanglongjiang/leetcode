'''
[TOC]

# 思路
模拟

# 解题方法
简单模拟

# 复杂度
- 时间复杂度: 
> $O(logn)$ 

- 空间复杂度: 
> $O(1)$
'''

from collections import Counter


class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        if len(s) != 9:
            return False
        c = Counter(s)
        if len(c) == 9 and c['0'] <= 0:
            return True
        return False

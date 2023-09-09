'''
[TOC]

# 思路
哈希表

# 解题方法
由于奇数下标只能和奇数下标，偶数下标只能和偶数下标交换，所以分别统计奇数下标和偶数下标的元素，对比

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n)$
'''

from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        c11, c12, c21, c22 = Counter(), Counter(), Counter(), Counter()
        i = 0
        for ch1, ch2 in zip(s1, s2):
            if i:
                c11[ch1] += 1
                c21[ch2] += 1
            else:
                c12[ch1] += 1
                c22[ch2] += 1
            i ^= 1
        return c11 == c21 and c12 == c22

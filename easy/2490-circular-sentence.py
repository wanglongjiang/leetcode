'''
[TOC]

# 思路
模拟

# 解题方法

遍历字符串，按照规则检查

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(1)$
'''


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        for i in range(len(sentence)):
            if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
                return False
        return True

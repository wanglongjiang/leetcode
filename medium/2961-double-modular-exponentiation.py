from typing import List

'''
[TOC]

# 思路
模拟

# 解题方法
模拟题意进行运算

# 复杂度
- 时间复杂度: 
> $O(n)$ 

- 空间复杂度: 
> $O(n)$
'''
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [i for i,(a,b,c,m) in enumerate(variables) if (a**b%10)**c%m == target]
    
s=Solution()
assert s.getGoodIndices(variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2)==[0,2]
assert s.getGoodIndices(variables = [[39,3,1000,1000]], target = 17)==[]

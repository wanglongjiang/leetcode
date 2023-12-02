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


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            d, r = divmod(mainTank, 5)
            ans += (mainTank - r) * 10
            mainTank = min(d, additionalTank) + r
            additionalTank -= min(d, additionalTank)
        ans += mainTank * 10
        return ans

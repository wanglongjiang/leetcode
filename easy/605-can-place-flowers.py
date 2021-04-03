'''
种花问题
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，
能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
'''
from typing import List
'''
思路：贪心算法
从左往右遍历，遇到的每个0，如果左右均没有1，则设置上。
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        i = 0
        while i < size:
            if flowerbed[i]:
                i += 1
                continue
            if i > 0:
                if flowerbed[i - 1] != 0:
                    i += 1
                    continue
            if i + 1 < size:
                if flowerbed[i + 1] != 0:
                    i += 3  # i+1为1，i+2邻接1，需要直接跳到i+3
                    continue
            n -= 1
            if n == 0:
                return True
            i += 2
        return False


s = Solution()
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
print(s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2))

'''
格雷编码
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。

格雷编码序列必须以 0 开头。
'''

from typing import List
'''
思路：组合。将格雷编码看从000开始，向0中逐步填充1的过程

'''


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        ans = []
        needFill = set([0])
        maxBit = 1 << n
        while needFill:
            ans.extend(needFill)
            newNeed = set()
            for num in needFill:
                bit = 1
                while bit < maxBit:
                    newNum = bit | num
                    if newNum != num:
                        newNeed.add(newNum)
                    bit <<= 1
            needFill = newNeed
        return ans


s = Solution()
print(s.grayCode(1))
print(s.grayCode(2))
print(s.grayCode(3))

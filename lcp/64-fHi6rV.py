from typing import List
'''
[TOC]

# 思路
暴力模拟

# 解题方法

1. 遍历矩阵的每一个空位
2. 检查是否能够改变该空位（检查行、列、对角线上，另外一端也是黑棋，能够将中间的白棋变为黑棋）
3. 改变该位置为黑棋，然后将中间的白棋变为黑棋
4. 将上述改变的白棋位置递归检查是否还有白棋变为黑棋

# 复杂度
- 时间复杂度: 
> $O(n*m*(n+m))$ 

- 空间复杂度: 
> $O(n*m)$
'''


class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        m, n = len(chessboard), len(chessboard[0])
        ans = 0

        def check():
            pass

        for i in range(m):
            for j in range(n):
                if chessboard[i][j] == '.':
                    # 检查行上是否
                    pass
        return ans

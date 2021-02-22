'''
N皇后 II

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

'''
from typing import List
'''
思路：回溯，调用51题的算法
'''


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        matirx = [[]] * n
        for i in range(n):
            matirx[i] = [0] * n

        # 判断是否合法的位置,只需要向上搜索同列、左上斜线、右上斜线
        def isValid(row, col):
            left, mid, right = col - 1, col, col + 1
            for row in range(row - 1, -1, -1):
                if left >= 0 and matirx[row][left] == 1:
                    return False
                else:
                    left -= 1
                if matirx[row][mid] == 1:
                    return False
                if right < n and matirx[row][right] == 1:
                    return False
                else:
                    right += 1
            return True

        # 回溯算法
        self.ansCount = 0

        def queens(row: int):
            for i in range(n):
                # 本位置如果合法，判断是否为最后一行，如果是最后一行，将结果输出，否则进行下一行
                if isValid(row, i):
                    matirx[row][i] = 1
                    if row == n - 1:
                        self.ansCount += 1
                    else:
                        queens(row + 1)
                    matirx[row][i] = 0

        queens(0)
        return self.ansCount


s = Solution()
print(s.totalNQueens(1))
print(s.totalNQueens(2))
print(s.totalNQueens(3))
print(s.totalNQueens(4))

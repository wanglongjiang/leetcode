'''
面试题 08.12. 八皇后
设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。
这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

注意：本题相对原题做了扩展

示例:

 输入：4
 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''
from typing import List
'''
思路：回溯 哈希
回溯每个数字将其放置到该行的不同列上，确保同列、同正对角线，同反对角线没有重复的皇后存在。
如何判断同列：用一个hashset保存已被占用的列
如何判断同对角线：用hashset保存col+row
如何判断同反对角线：用hashset保存col-row

类似的题目：
- 51.[N 皇后](hard/51-n-queens.py)
- 52.[N 皇后 II](hard/52-n-queens-ii.py)

时间复杂度：O(n^n)
空间复杂度：O(n^2)
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.'] * n for _ in range(n)]
        cols, slash, backslash = set(), set(), set()

        def backtrack(i):
            for j in range(n):
                if j not in cols and (i - j) not in slash and (i + j) not in backslash:  # 如果该位置是一个合法位置，占据
                    board[i][j] = 'Q'
                    cols.add(j)
                    slash.add(i - j)
                    backslash.add(i + j)
                    if i < n - 1:
                        backtrack(i + 1)
                    else:  # 找到合法的解，输出到结果中
                        ans.append(list(map(lambda row: ''.join(row), board)))
                    backslash.remove(i + j)
                    slash.remove(i - j)
                    cols.remove(j)
                    board[i][j] = '.'

        backtrack(0)
        return ans


s = Solution()
print(s.solveNQueens(4))

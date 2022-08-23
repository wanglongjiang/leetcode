'''
782. 变为棋盘
一个 n x n 的二维网络 board 仅由 0 和 1 组成 。每次移动，你能任意交换两列或是两行的位置。

返回 将这个矩阵变为  “棋盘”  所需的最小移动次数 。如果不存在可行的变换，输出 -1。

“棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。

 

示例 1:



输入: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
输出: 2
解释:一种可行的变换方式如下，从左到右：
第一次移动交换了第一列和第二列。
第二次移动交换了第二行和第三行。
示例 2:



输入: board = [[0, 1], [1, 0]]
输出: 0
解释: 注意左上角的格值为0时也是合法的棋盘，也是合法的棋盘.
示例 3:



输入: board = [[1, 0], [1, 0]]
输出: -1
解释: 任意的变换都不能使这个输入变为合法的棋盘。
 

提示：

n == board.length
n == board[i].length
2 <= n <= 30
board[i][j] 将只包含 0或 1
'''
from typing import List

from collections import Counter
'''
思路：
'''


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # 将行列转为二进制数：交换行列不会影响位运算的异或运算与与运算
        row = []
        for i in range(n):
            for j in range(n):
                board[i][j] = str(board[i][j])
            row.append(int("0b" + "".join(board[i]), 2))

        col = []
        for j in range(n):
            col.append(int("0b" + "".join([board[i][j] for i in range(n)]), 2))

        def check(lst):
            cnt = Counter(lst)
            x, y = min(cnt), max(cnt)
            # 不满足条件：只有两个数
            if len(cnt) != 2:
                return -1
            # 不满足条件：位运算不是互补
            if x & y or x ^ y != (1 << n) - 1:
                return -1
            # 不满足条件：奇偶个数
            if n % 2 == 0:
                if cnt[x] != cnt[y]:
                    return -1
            else:
                if abs(cnt[x] - cnt[y]) != 1:
                    return -1
            # 列举可能的顺序组合：计算需要操作的次数
            lst1 = []
            lst2 = []
            for k in range(n):
                if k % 2:
                    lst1.append(x)
                    lst2.append(y)
                else:
                    lst1.append(y)
                    lst2.append(x)
            # 贪心比较不同位置的个数：由于两个数一定是成对出现所以除以2即为操作次数
            if Counter(lst1) == cnt:
                cost1 = sum(int(lst[k] != lst1[k]) for k in range(n)) // 2
            else:
                cost1 = n + 1
            if Counter(lst2) == cnt:
                cost2 = sum(int(lst[k] != lst2[k]) for k in range(n)) // 2
            else:
                cost2 = n + 1
            return min(cost1, cost2)

        row_cost = check(row)
        col_cost = check(col)
        if row_cost == -1 or col_cost == -1:
            return -1
        return row_cost + col_cost

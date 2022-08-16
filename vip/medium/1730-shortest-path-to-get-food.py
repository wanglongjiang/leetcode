'''
1730. 获取食物的最短路径
你现在很饿，想要尽快找东西吃。你需要找到最短的路径到达一个食物所在的格子。

给定一个 m x n 的字符矩阵 grid ，包含下列不同类型的格子：

'*' 是你的位置。矩阵中有且只有一个 '*' 格子。
'#' 是食物。矩阵中可能存在多个食物。
'O' 是空地，你可以穿过这些格子。
'X' 是障碍，你不可以穿过这些格子。
返回你到任意食物的最短路径的长度。如果不存在你到任意食物的路径，返回 -1。



示例 1:


输入： grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
输出： 3
解释： 要拿到食物，你需要走 3 步。
Example 2:


输入： grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
输出： -1
解释： 你不可能拿到食物。
示例 3:


输入: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],
["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
输出: 6
解释: 这里有多个食物。拿到下边的食物仅需走 6 步。
示例 4:

输入: grid = [["O","*"],["#","O"]]
输出: 2
示例 5:

输入: grid = [["X","*"],["#","X"]]
输出: -1


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] 是 '*'、 'X'、 'O' 或 '#' 。
grid 中有且只有一个 '*' 。
'''
from typing import List
'''
思路：BFS
典型的bfs题目，套路解题。

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':  # 找到自身所在单元格，用bfs查找最近的食物距离
                    q, nextq = [(i, j)], []
                    marked = set()
                    marked.add((i, j))
                    dis = 0
                    while q:
                        i, j = q.pop()
                        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                            if 0 <= x < m and 0 <= y < n and (x, y) not in marked:
                                if grid[x][y] == '#':
                                    return dis + 1
                                elif grid[x][y] == 'O':
                                    nextq.append((x, y))
                                    marked.add((x, y))
                        if not q:
                            q, nextq = nextq, q
                            dis += 1
                    return -1


s = Solution()
print(s.getFood([["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O", "X"], ["X", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X"]]))
print(s.getFood([["X", "X", "X", "X", "X"], ["X", "*", "X", "O", "X"], ["X", "O", "X", "#", "X"], ["X", "X", "X", "X", "X"]]))
print(
    s.getFood([["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "*", "O", "X", "O", "#", "O", "X"], ["X", "O", "O", "X", "O", "O", "X", "X"],
               ["X", "O", "O", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"]]))
print(s.getFood([["O", "*"], ["#", "O"]]))
print(s.getFood([["X", "*"], ["#", "X"]]))

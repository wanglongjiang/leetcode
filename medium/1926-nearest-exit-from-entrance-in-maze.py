'''
迷宫中离入口最近的出口
给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。
同时给你迷宫的入口 entrance ，用 entrance = [entrancerow, entrancecol] 表示你一开始所在格子的行和列。

每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 entrance 最近 的出口。
出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。

请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1 。

 

示例 1：


输入：maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
输出：1
解释：总共有 3 个出口，分别位于 (1,0)，(0,2) 和 (2,3) 。
一开始，你在入口格子 (1,2) 处。
- 你可以往左移动 2 步到达 (1,0) 。
- 你可以往上移动 1 步到达 (0,2) 。
从入口处没法到达 (2,3) 。
所以，最近的出口是 (0,2) ，距离为 1 步。
示例 2：


输入：maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
输出：2
解释：迷宫中只有 1 个出口，在 (1,2) 处。
(1,0) 不算出口，因为它是入口格子。
初始时，你在入口与格子 (1,0) 处。
- 你可以往右移动 2 步到达 (1,2) 处。
所以，最近的出口为 (1,2) ，距离为 2 步。
示例 3：


输入：maze = [[".","+"]], entrance = [0,0]
输出：-1
解释：这个迷宫中没有出口。
 

提示：

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] 要么是 '.' ，要么是 '+' 。
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance 一定是空格子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nearest-exit-from-entrance-in-maze
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import collections
'''
思路：BFS
用BFS遍历矩阵，直至遇到边界，返回此时的路径长度，或者没有路径，返回-1

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        marked = [[False] * n for _ in range(m)]
        marked[entrance[0]][entrance[1]] = True
        q, nextq = collections.deque(), collections.deque()
        q.append((entrance[0], entrance[1]))
        ans = 0
        while q:
            i, j = q.popleft()
            for nexti, nextj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nexti < m and 0 <= nextj < n and not marked[nexti][nextj] and maze[nexti][nextj] == '.':
                    if nexti == 0 or nexti == m - 1 or nextj == 0 or nextj == n - 1:
                        return ans + 1
                    marked[nexti][nextj] = True
                    nextq.append((nexti, nextj))
            if not q:
                q, nextq = nextq, q
                ans += 1
        return -1


s = Solution()
print(s.nearestExit(maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], entrance=[1, 2]))
print(s.nearestExit(maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance=[1, 0]))
print(s.nearestExit(maze=[[".", "+"]], entrance=[0, 0]))

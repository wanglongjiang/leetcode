'''
1254. 统计封闭岛屿的数目
二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目。

 

示例 1：



输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
示例 2：



输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1
示例 3：

输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2
 

提示：

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''
from inspect import isclass
from typing import List
'''
思路：DFS
从每个陆地单元格出发，用DFS遍历，如果遍历过程中经过边界，该岛屿不是封闭的

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        marked = [[False] * n for _ in range(m)]

        def dfs(i, j):
            marked[i][j] = True
            isClosed = not (i == 0 or i == m - 1 or j == 0 or j == n - 1)
            for nexti, nextj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nexti < m and 0 <= nextj < n and grid[nexti][nextj] == 0 and not marked[nexti][nextj]:
                    if not dfs(nexti, nextj):
                        isClosed = False
            return isClosed

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not marked[i][j] and dfs(i, j):
                    ans += 1
        return ans


s = Solution()
print(s.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))

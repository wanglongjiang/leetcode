'''
岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
'''
from typing import List
'''
思路1，遍历grid所有单元格，遇到1，岛屿数+1，深度搜索相邻的1并清空。
时间复杂度：O(m*n)
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islandNum = 0

        def clear(i, j):
            grid[i][j] = '0'
            if i > 0 and grid[i - 1][j] == '1':
                clear(i - 1, j)
            if j > 0 and grid[i][j - 1] == '1':
                clear(i, j - 1)
            if i + 1 < m and grid[i + 1][j] == '1':
                clear(i + 1, j)
            if j + 1 < n and grid[i][j + 1] == '1':
                clear(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islandNum += 1
                    clear(i, j)
        return islandNum


s = Solution()
print(s.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(s.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))

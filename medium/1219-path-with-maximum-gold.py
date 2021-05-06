'''
黄金矿工

你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。
每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

为了使收益最大化，矿工需要按以下规则来开采黄金：

每当矿工进入一个单元，就会收集该单元格中的所有黄金。
矿工每次可以从当前位置向上下左右四个方向走。
每个单元格只能被开采（进入）一次。
不得开采（进入）黄金数目为 0 的单元格。
矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
 

示例 1：

输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。
示例 2：

输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
 

提示：

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
最多 25 个单元格中有黄金。
'''
from typing import List
'''
思路：DFS
从任意节点出发，遍历所有路径，找到最大的2个路径和（因为不能重复走，所以只能选择最大的2个路径和）
时间复杂度：O(m*n*m*n)
空间复杂度：O(m*n)
TODO
'''


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        maxGold = 0

        def dfs(i, j, visited):
            nonlocal maxGold
            visited[i][j] = True
            path1 = 0
            path2 = 0
            for a, b in directs:
                x, y = a + i, b + j
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0 and not visited[x][y]:
                    g = dfs(x, y, visited)
                    if g > path1:
                        path2 = path1
                        path1 = g
                    elif g > path2:
                        path2 = g
            maxGold = max(maxGold, grid[i][j] + path1 + path2)
            return grid[i][j] + path1

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                if grid[i][j]:
                    dfs(i, j, visited)
        return maxGold


s = Solution()
print(
    s.getMaximumGold([[0, 0, 0, 22, 0, 24], [34, 23, 18, 0, 23, 2], [11, 39, 20, 12, 0, 0], [39, 8, 0, 2, 0, 1], [19, 32, 26, 20, 20, 30],
                      [0, 38, 26, 0, 29, 31]]))
print(s.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
print(s.getMaximumGold([[1, 0, 7, 0, 0, 0], [2, 0, 6, 0, 1, 0], [3, 5, 6, 7, 4, 2], [4, 3, 1, 0, 2, 0], [3, 0, 5, 0, 20, 0]]))
print(s.getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))

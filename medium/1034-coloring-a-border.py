'''
1034. 边界着色
给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数 row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。

两个网格块属于同一 连通分量 需满足下述全部条件：
两个网格块颜色相同
在上、下、左、右任意一个方向上相邻

连通分量的边界 是指连通分量中满足下述条件之一的所有网格块：
在上、下、左、右任意一个方向上与不属于同一连通分量的网格块相邻
在网格的边界上（第一行/列或最后一行/列）

请你使用指定颜色 color 为所有包含网格块 grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格 grid 。

 

示例 1：

输入：grid = [
    [1,1],
    [1,2]], row = 0, col = 0, color = 3
输出：[
    [3,3],
    [3,2]]
示例 2：

输入：grid = [
    [1,2,2],
    [2,3,2]], row = 0, col = 1, color = 3
输出：[
    [1,3,3],
    [2,3,3]]
示例 3：

输入：grid = [
    [1,1,1],
    [1,1,1],
    [1,1,1]], row = 1, col = 1, color = 2
输出：[
    [2,2,2],
    [2,1,2],
    [2,2,2]]
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j], color <= 1000
0 <= row < m
0 <= col < n
'''
from typing import List
from collections import deque
'''
思路：BFS
BFS遍历同一联通分量，如果是边界，将其着色

时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append((row, col))
        marked = [[False] * n for _ in range(m)]
        marked[row][col] = True
        while queue:
            row, col = queue.pop()
            # 将连通节点加入队列
            for nextRow, nextCol in filter(lambda p: p[0] >= 0 and p[0] < m and p[1] >= 0 and p[1] < n, [(row + 1, col), (row - 1, col), (row, col + 1),
                                                                                                         (row, col - 1)]):
                if not marked[nextRow][nextCol] and grid[row][col] == grid[nextRow][nextCol]:
                    queue.append((nextRow, nextCol))
                    marked[nextRow][nextCol] = True
            # 如果是矩阵边界，着色
            if row == 0 or row == m - 1 or col == 0 or col == n - 1:
                grid[row][col] = color
            else:
                for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if r >= 0 and r < m and c >= 0 and c < n:
                        if not marked[r][c] and grid[row][col] != grid[r][c]:  # 与相邻非连通节点相邻，也是边界，着色
                            grid[row][col] = color
                            break
        return grid


s = Solution()
print(s.colorBorder(grid=[[1, 1], [1, 2]], row=0, col=0, color=3) == [[3, 3], [3, 2]])
print(s.colorBorder(grid=[[1, 2, 2], [2, 3, 2]], row=0, col=1, color=3) == [[1, 3, 3], [2, 3, 3]])
print(s.colorBorder(grid=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], row=1, col=1, color=2) == [[2, 2, 2], [2, 1, 2], [2, 2, 2]])

'''
太平洋大西洋水流问题

给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

 

提示：

输出坐标的顺序不重要
m 和 n 都小于150
 

示例：

 

给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
'''
from typing import List
'''
思路：DFS
将矩阵边界处的单元格分别加入太平洋、大西洋的边界集合
然后遍历所有的单元格，DFS遍历所有可能的路径，查看是否有相邻节点在太平洋、大西洋的边界集合里面，如果存在，将其也加入太平洋、大西洋的边界集合
最后求出2个集合的交集，即为结果

时间复杂度：O(m*n)
空间复杂度：O(m*n)
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 将边界处单元格加入太平洋、大西洋集合
        pacific, atlantic = set(), set()
        m, n = len(heights), len(heights[0])
        for i in range(0, n):
            pacific.add(i)
            atlantic.add((m - 1) * n + i)
        for i in range(0, m):
            pacific.add(i * n)
            atlantic.add(i * n + n - 1)

        # 遍历所有的单元格，将其加入能流向的大洋集合
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            visited[i][j] = True
            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = a + i, b + j
                if 0 <= x < m and 0 <= y < n and heights[x][y] <= heights[i][j]:
                    if not visited[x][y]:
                        dfs(x, y)
                    nextPos = x * n + y
                    thisPos = i * n + j
                    if nextPos in pacific:  # 如果下一个单元格能流向某个大洋，则当前单元格也可以
                        pacific.add(thisPos)
                    if nextPos in atlantic:  # 如果下一个单元格能流向某个大洋，则当前单元格也可以
                        atlantic.add(thisPos)

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    dfs(i, j)
        # 遍历2个大洋的交集
        ans = []
        for pos in pacific & atlantic:
            i, j = divmod(pos, n)
            ans.append([i, j])
        return ans


s = Solution()
print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))

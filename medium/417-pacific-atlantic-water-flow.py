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
from collections import deque
from typing import List

from numpy import true_divide
'''
思路：BFS
将矩阵边界处的单元格分别加入太平洋、大西洋的边界集合
然后遍历所有的单元格，BFS遍历所有可能的路径，查看是否有相邻节点在太平洋、大西洋的边界集合里面，如果存在，将其也加入太平洋、大西洋的边界集合
最后求出2个集合的交集，即为结果

时间复杂度：O(m*n)
空间复杂度：O(m*n)
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 将边界处单元格加入太平洋、大西洋集合
        pacific, atlantic = set(), set()
        m, n = len(heights), len(heights[0])
        queuep, queuea = deque(), deque()
        for i in range(0, n):
            pacific.add((0, i))
            atlantic.add((m - 1, i))
            queuep.append((0, i))
            queuea.append((m - 1, i))
        for i in range(0, m):
            pacific.add((i, 0))
            atlantic.add((i, n - 1))
            queuep.append((i, 0))
            queuea.append((i, n - 1))

        visited = [[False] * n for _ in range(m)]

        while queuep:
            i, j = queuep.popleft()
            visited[i][j] = True
            for nextpos in [item for item in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if 0 <= item[0] < m and 0 <= item[1] < n]:
                if heights[nextpos[0]][nextpos[1]] >= heights[i][j]:  # 如果下个位置高于当前位置，水可以从下一个位置流过来
                    if (i, j) in pacific:
                        pacific.add(nextpos)
                    if not visited[nextpos[0]][nextpos[1]]:
                        queuep.append(nextpos)
        visited = [[False] * n for _ in range(m)]
        while queuea:
            i, j = queuea.popleft()
            visited[i][j] = True
            for nextpos in [item for item in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if 0 <= item[0] < m and 0 <= item[1] < n]:
                if heights[nextpos[0]][nextpos[1]] >= heights[i][j]:  # 如果下个位置高于当前位置，水可以从下一个位置流过来
                    if (i, j) in atlantic:
                        atlantic.add(nextpos)
                    if not visited[nextpos[0]][nextpos[1]]:
                        queuea.append(nextpos)
        # 遍历2个大洋的交集
        ans = []
        for pos in pacific & atlantic:
            ans.append([pos[0], pos[1]])
        return ans


s = Solution()
print(s.pacificAtlantic([[3, 3, 3, 3, 3, 3], [3, 0, 3, 3, 0, 3], [3, 3, 3, 3, 3, 3]]))
print(
    s.pacificAtlantic([[10, 10, 1, 11, 2, 15, 17, 6, 17, 10, 0, 10, 18, 9, 16, 13, 8, 9, 12, 6, 3, 2, 5, 19, 4, 14],
                       [12, 19, 13, 2, 7, 2, 3, 8, 17, 4, 2, 1, 8, 13, 7, 2, 10, 16, 12, 3, 4, 12, 4, 16, 0, 12],
                       [1, 12, 9, 18, 12, 16, 17, 5, 13, 0, 7, 13, 12, 13, 6, 2, 11, 19, 7, 2, 6, 11, 11, 0, 17, 6],
                       [1, 12, 2, 0, 11, 7, 7, 3, 7, 13, 11, 1, 11, 15, 5, 13, 14, 12, 4, 10, 5, 16, 3, 17, 18, 12],
                       [9, 16, 11, 5, 9, 13, 7, 18, 18, 14, 19, 10, 9, 4, 8, 14, 4, 19, 13, 1, 14, 8, 0, 3, 12, 10],
                       [10, 19, 9, 11, 1, 18, 1, 2, 1, 8, 1, 5, 2, 15, 14, 13, 18, 18, 11, 4, 15, 3, 15, 12, 12, 2],
                       [0, 10, 9, 2, 15, 9, 12, 7, 0, 0, 12, 18, 9, 12, 18, 4, 18, 10, 3, 1, 17, 14, 13, 18, 9, 4],
                       [3, 19, 9, 16, 16, 19, 11, 19, 6, 9, 18, 0, 12, 11, 13, 1, 15, 6, 9, 18, 9, 6, 3, 12, 12, 2],
                       [0, 16, 15, 12, 3, 19, 18, 9, 5, 1, 4, 3, 19, 15, 1, 0, 7, 10, 14, 4, 8, 10, 15, 16, 14, 8],
                       [15, 9, 3, 15, 19, 17, 17, 10, 9, 8, 16, 11, 3, 15, 15, 9, 1, 14, 11, 13, 16, 7, 1, 7, 13, 5],
                       [9, 19, 6, 7, 19, 14, 4, 18, 6, 10, 19, 13, 12, 7, 7, 15, 6, 10, 7, 8, 8, 8, 19, 13, 17, 14],
                       [14, 7, 1, 15, 2, 6, 12, 4, 2, 19, 17, 17, 8, 9, 19, 10, 0, 12, 4, 12, 4, 16, 15, 18, 8, 0],
                       [4, 8, 5, 8, 0, 2, 19, 18, 1, 7, 13, 9, 13, 16, 6, 15, 15, 12, 18, 5, 8, 11, 6, 17, 5, 11],
                       [17, 16, 9, 19, 12, 6, 13, 19, 0, 6, 7, 9, 7, 13, 9, 18, 5, 15, 16, 8, 18, 9, 6, 0, 11, 14],
                       [11, 5, 13, 3, 12, 19, 5, 15, 2, 15, 9, 16, 6, 12, 8, 0, 19, 19, 11, 0, 16, 8, 15, 15, 1, 12],
                       [15, 16, 16, 19, 14, 1, 2, 11, 14, 8, 16, 13, 2, 0, 3, 8, 1, 5, 4, 15, 12, 5, 13, 3, 5, 3]]))
print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))

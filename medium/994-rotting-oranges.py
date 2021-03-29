'''
腐烂的橘子

在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

提示：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 仅为 0、1 或 2
'''
from typing import List
'''
思路：广度优先搜索。
遍历一次矩阵，将所有烂橘子加入队列，然后按照BFS开始搜索。如果所有的路径都走完，还有好橘子存在，则返回-1。
时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 将所有烂橘子找出
        badQueue = []
        good = set()
        m, n = len(grid), len(grid[0])
        marked = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    badQueue.append((i, j))
                    marked[i][j] = 1  # 腐烂橘子的默认为1，是为了方便计算，最后返回结果时需要减一
                elif grid[i][j] == 0:
                    marked[i][j] = True
                else:
                    good.add(i * n + j)
        if len(good) == 0:
            return 0
        # BFS遍历
        index = 0
        time = 0
        while index < len(badQueue) and len(good) > 0:
            i, j = badQueue[index]
            index += 1
            # 向4个方向移动
            if i > 0 and not marked[i - 1][j]:
                marked[i - 1][j] = marked[i][j] + 1
                badQueue.append((i - 1, j))
                good.remove((i - 1) * n + j)
                time = max(time, marked[i][j] + 1)
            if i + 1 < m and not marked[i + 1][j]:
                marked[i + 1][j] = marked[i][j] + 1
                badQueue.append((i + 1, j))
                good.remove((i + 1) * n + j)
                time = max(time, marked[i][j] + 1)
            if j > 0 and not marked[i][j - 1]:
                marked[i][j - 1] = marked[i][j] + 1
                badQueue.append((i, j - 1))
                good.remove(i * n + j - 1)
                time = max(time, marked[i][j] + 1)
            if j + 1 < n and not marked[i][j + 1]:
                marked[i][j + 1] = marked[i][j] + 1
                badQueue.append((i, j + 1))
                good.remove(i * n + j + 1)
                time = max(time, marked[i][j] + 1)
        if len(good) > 0:
            return -1
        return time - 1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(s.orangesRotting([[0, 2]]))

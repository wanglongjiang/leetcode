'''
地图中的最高点
给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。

如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。
你需要按照如下规则给每个单元格安排高度：

每个格子的高度都必须是非负的。
如果一个格子是是 水域 ，那么它的高度必须为 0 。
任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。
（也就是说它们有一条公共边）
找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。

请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。
如果有多种解法，请返回 任意一个 。


提示：

m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] 要么是 0 ，要么是 1 。
至少有 1 个水域格子。
'''
from typing import List
'''
思路：BFS
从所有的水域出发，广度优先遍历所有的格子，距离每远1步，高度+1
时间复杂度：O(mn)
空间复杂度：O(mn)
'''


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = []
        m, n = len(isWater), len(isWater[0])
        heights = [[0] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        # 将所有水域加入队列
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    visited[i][j] = True
                    queue.append((i, j))
        # BFS遍历所有格子
        nextqueue = []
        height = 1
        while queue:
            i, j = queue.pop()
            if i > 0:
                if not visited[i - 1][j]:
                    visited[i - 1][j] = True
                    heights[i - 1][j] = height
                    nextqueue.append((i - 1, j))
            if j > 0:
                if not visited[i][j - 1]:
                    visited[i][j - 1] = True
                    heights[i][j - 1] = height
                    nextqueue.append((i, j - 1))
            if i < m - 1:
                if not visited[i + 1][j]:
                    visited[i + 1][j] = True
                    heights[i + 1][j] = height
                    nextqueue.append((i + 1, j))
            if j < n - 1:
                if not visited[i][j + 1]:
                    visited[i][j + 1] = True
                    heights[i][j + 1] = height
                    nextqueue.append((i, j + 1))
            if not queue:  # 当前待遍历的队列为空，需要遍历更远距离，更远的距离的格子高度+1
                queue = nextqueue
                nextqueue = []
                height += 1
        return heights


s = Solution()
print(s.highestPeak([[0, 1], [0, 0]]))
print(s.highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))

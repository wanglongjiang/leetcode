'''
最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
'''
from typing import List
'''
思路1，Dijkstra算法
该问题看作是有向图的最短路径，可以用经典的Dijkstra算法。
Dijkstra算法使用贪心策略，每次都从路径中选择最短的一个向后前进
时间复杂度：O(mn)，初始化图O(mn)，最短路径搜索需要O(logmn)，最小堆提取元素、deckey需要O(logmn)
空间复杂度：O(mn)，因为每个节点只有向左，向下2个边，所以邻接表的空间复杂度为O(mn)，原点到所有节点的最短路径也是O(mn)


思路2，广度优先遍历算法
该问题看作是有向图的最短路径，可以用广度优先搜索算法。
时间复杂度：O(mn)，初始化图O(mn)，搜索最短路径需要O(mn)
空间复杂度：O(mn)，因为每个节点只有向左，向下2个边，所以邻接表的空间复杂度为O(mn)，原点到所有节点的最短路径也是O(mn)
'''


class Solution:
    # 思路2，广度优先算法
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 矩阵中每个单元格为一个节点，使用邻接表表示图，每个节点的id为rowNum*n+colNum
        g = [[] for i in range(m * n)]
        # 初始化图的边，边中存储(下一节点id,到下一节点的距离),2个节点的距离为矩阵中下一个节点的值
        for i in range(m):
            for j in range(n):
                if j + 1 < n:
                    g[i * n + j].append((i * n + j + 1, grid[i][j + 1]))  # 向左的边
                if i + 1 < m:
                    g[i * n + j].append(((i + 1) * n + j, grid[i + 1][j]))  # 向右的边
        # 原点到各节点最短路径用数组表示，初始都是无穷大
        d = [float('inf')] * m * n
        d[0] = grid[0][0]  # 原点的路径长度为grid[0][0]的值
        # 广度优先搜索需要辅助队列
        queue = []
        queue.append(0)  # 从第0个开始搜索
        target = m * n - 1
        while queue:
            i = queue[0]
            del queue[0]
            for nodeid, w in g[i]:  # 遍历i节点的所有边
                d[nodeid] = min(d[nodeid], d[i] + w)
                queue.append(nodeid)
        return d[target]

    # 思路1，Dijkstra算法
    def minPathSum1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 矩阵中每个单元格为一个节点，使用邻接表表示图，每个节点的id为rowNum*n+colNum
        g = [[] for i in range(m * n)]
        # 初始化图的边，边中存储(下一节点id,到下一节点的距离),2个节点的距离为矩阵中下一个节点的值
        for i in range(m):
            for j in range(n):
                if j + 1 < n:
                    g[i * n + j].append((i * n + j + 1, grid[i][j + 1]))  # 向左的边
                if i + 1 < m:
                    g[i * n + j].append(((i + 1) * n + j, grid[i + 1][j]))  # 向右的边
        # 原点到各节点路径长度用数组表示，初始都是无穷大
        d = [float('inf')] * m * n
        d[0] = grid[0][0]  # 原点的路径长度为grid[0][0]的值

        # 建立最小堆
        minHeap = MinHeap(m * n, d)

        # 松弛函数，松弛节点u到v的距离
        def relax(u, v):
            w = g[u][0][1] if g[u][0][0] == v else g[u][1][1]
            if d[v] > d[u] + w:
                minHeap.decKey(v, d[u] + w)

        # 开始搜索最短路径
        target = m * n - 1
        while True:
            u = minHeap.extractMin()  # 每次都提取路径最小的节点u
            for nodeid, w in g[u]:  # 遍历u的所有边，松弛其路径大小
                relax(u, nodeid)
                if nodeid == target:  # 如果找到了终点，结束所有处理
                    return d[target]


# 最小堆，Dijkstra算法下用于存放原点到各节点路径的下标
class MinHeap():
    def __init__(self, size, d):
        # 第0个元素最小，其他元素都是正无穷大，默认就是最小堆
        self.heap = [i for i in range(size)]
        self.size = size
        self.d = d
        self.nodeIdMap = {}
        for i in range(self.size):
            self.nodeIdMap[i] = i

    # 从堆中删除最小元素并返回
    def extractMin(self):
        i = self.heap[0]
        self.size = self.size - 1
        self.heap[0] = self.heap[-1]
        self.minHeapify(0)
        return i

    # 减少最小堆里面的一个节点的值
    def decKey(self, nodeid, val):
        self.d[nodeid] = val
        heapIndex = self.nodeIdMap[nodeid]
        parent = (heapIndex - 1) // 2
        while heapIndex > 0 and self.d[self.heap[parent]] > self.d[self.heap[heapIndex]]:
            self.nodeIdMap[self.heap[parent]] = heapIndex
            self.nodeIdMap[self.heap[heapIndex]] = parent
            self.heap[parent], self.heap[heapIndex] = self.heap[heapIndex], self.heap[parent]
            heapIndex, parent = parent, (parent - 1) // 2

    # 保持最小堆的性质
    def minHeapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minIndex = i
        # 如果左、右子节点指向的路径小于父节点的路径，不满足最小堆性质，需要将父节点与左或右节点交换，使之满足最小堆性质
        if left < self.size and self.d[self.heap[left]] < self.d[self.heap[minIndex]]:
            minIndex = left
        if right < self.size and self.d[self.heap[right]] < self.d[self.heap[minIndex]]:
            minIndex = right
        if minIndex != i:
            self.nodeIdMap[self.heap[minIndex]] = i
            self.nodeIdMap[self.heap[i]] = minIndex
            self.heap[minIndex], self.heap[i] = self.heap[i], self.heap[minIndex]
            self.minHeapify(minIndex)  # 交换后子节点可能不满足最小堆性质，需要递归向下执行


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))

'''
最小体力消耗路径
你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。
一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。
你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

请你返回从左上角走到右下角的最小 体力消耗值 。

提示：
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 10^6
'''
from typing import List
'''
思路：Dijkstra计算最短路径
经典的无向有权图的求解问题，使用Dijkstra算法
Dijkstra算法是一种贪心算法，它设置一个数组d，保存原点到各单元格的路径长度
用最小堆从d中提取路径最小的单元格g，然后对从g出发的路径进行松弛relax。
重复上面的过程，直至找到终点。
时间复杂度：O(mn*logmn)，最坏情况下需要遍历m*n，每次访问最小堆的时间复杂度O(logmn)
空间复杂度：O(mn)，保存路径长度的数组d大小为m*n，保存单元格是否遍历过的数组v大小为m*n，最小堆大小为m*n
'''


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        d = [float('inf')] * rows * cols  # 保存从节点0到该单元格的路径长度
        d[0] = 0
        heap = MinHeap(rows * cols, d)  # 建立最小堆，最小堆用于选择距离0最小的元素

        # 松弛函数，松弛2个节点的距离
        def relax(u, v):
            w = abs(heights[u // cols][u % cols] - heights[v // cols][v % cols])  # 两个节点的距离为2个节点的高度差
            if max(d[u], w) < d[v]:
                heap.decKey(v, max(d[u], w))  # 将d[v]，也就是v节点到0点的距离更新为d[u]+w

        end = rows * cols - 1
        while heap.size > 0:
            u = heap.extractMin()
            i, j = divmod(u, cols)
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                nextpos = x * cols + y
                if 0 <= x < rows and 0 <= y < cols:
                    relax(u, nextpos)
                    if u == end:
                        return d[u]
        return d[end]


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
        if self.size > 0:
            self.heap[0] = self.heap[self.size]
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
print(s.minimumEffortPath([[3]]))
print(s.minimumEffortPath([[3], [3], [7], [2], [9], [9], [3], [7], [10]]))
print(s.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(s.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(s.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))

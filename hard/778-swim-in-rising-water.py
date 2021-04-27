'''
水位上升的泳池中游泳
在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，
但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。
当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

提示:

2 <= N <= 50.
grid[i][j] 是 [0, ..., N*N - 1] 的排列。
'''
from typing import List
'''
思路：并查集+最小堆
1、将单元格坐标加入最小堆，按照高度排序
2、运行一个0..N*N - 1的循环，模拟时间的变化
3、在循环体内部，提取高度最小的单元格grid[i][j]，将其与相邻且在水面以下的单元格加入并查集，
    再判断如果右下角与0,0是处在同一个集合内，返回当前时间
时间复杂度：O(n*nlog(n*n))
空间复杂度：O(n*n)
'''


# 定义最小堆
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    # 向堆中插入值
    def insert(self, item):
        self.heap.append(item)
        i = self.size
        self.size += 1
        while i > 0 and self.heap[self.parent(i)][0] > item[0]:  # 将小于父节点的值向上提升
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # 从堆中删除最小元素并返回
    def extractMin(self):
        i = self.heap[0]
        self.size -= 1
        last = self.heap.pop()
        if self.size:
            self.heap[0] = last
        self.minHeapify(0)
        return i

    # 保持最小堆的性质
    def minHeapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minIndex = i
        # 如果左、右子节点小于父节点，不满足最小堆性质，需要将父节点与左或右节点交换，使之满足最小堆性质
        if left < self.size and self.heap[left][0] < self.heap[minIndex][0]:
            minIndex = left
        if right < self.size and self.heap[right][0] < self.heap[minIndex][0]:
            minIndex = right
        if minIndex != i:
            self.heap[minIndex], self.heap[i] = self.heap[i], self.heap[minIndex]
            self.minHeapify(minIndex)  # 交换后子节点可能不满足最小堆性质，需要递归向下执行

    # 求父节点的索引
    def parent(self, i):
        return (i - 1) // 2

    def getMin(self):
        return self.heap[0]

    def notEmpty(self):
        return self.size > 0


# 定义并查集
class UnionSet:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:  # 确保较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        end = n * n - 1
        heap = MinHeap()
        union = UnionSet(n * n)
        # 1、将单元格坐标加入最小堆，按照高度排序
        for i in range(n):
            for j in range(n):
                heap.insert((grid[i][j], (i, j)))
        # 2、运行一个0..N*N - 1的循环，模拟时间的变化
        for t in range(n * n):
            a, b = heap.extractMin()[1]
            # 3、提取高度最小的单元格grid[i][j]，将其与相邻且在水面以下的单元格加入并查集，
            for x, y in [(a - 1, b), (a, b - 1), (a + 1, b), (a, b + 1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] < t:
                    union.unite(a * n + b, x * n + y)
            if grid[-1][-1] <= t and union.find(end) == 0:
                return t


s = Solution()
print(s.swimInWater([[0, 2], [1, 3]]))
print(s.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))

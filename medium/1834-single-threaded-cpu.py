'''
单线程 CPU
给你一个二维数组 tasks ，用于表示 n​​​​​​ 项从 0 到 n - 1 编号的任务。其中 tasks[i] = [enqueueTimei, processingTimei] 
意味着第 i​​​​​​​​​​ 项任务将会于 enqueueTimei 时进入任务队列，需要 processingTimei 的时长完成执行。

现有一个单线程 CPU ，同一时间只能执行 最多一项 任务，该 CPU 将会按照下述方式运行：

如果 CPU 空闲，且任务队列中没有需要执行的任务，则 CPU 保持空闲状态。
如果 CPU 空闲，但任务队列中有需要执行的任务，则 CPU 将会选择 执行时间最短 的任务开始执行。
如果多个任务具有同样的最短执行时间，则选择下标最小的任务开始执行。
一旦某项任务开始执行，CPU 在 执行完整个任务 前都不会停止。
CPU 可以在完成一项任务后，立即开始执行一项新任务。
返回 CPU 处理任务的顺序。

 
提示：

tasks.length == n
1 <= n <= 10^5
1 <= enqueueTimei, processingTimei <= 10^9
'''
from typing import List
'''
思路：最小堆+模拟
1、初始化当前时刻为第1个任务的进入队列时间，从队列中遍历出进入队列最近的几个任务加入最小堆（先比较运行时间，运行时间相同的比较索引）
2、从最小堆中取出最小的任务运行（将当前时间+任务运行时间）
3、然后再从队列中提取小于当前时间的任务加入最小堆。重复上面过程2。
说明，最小堆能挑选出正确的任务的原因是，当前时间>=任务进入队列时间，对于这种任务，
调度它的因素首先考虑运行时间，其次考虑原索引。

时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        heap = MinHeap()
        curTime = 0
        i, n = 0, len(tasks)
        while i < n:
            if heap.isEmpty():  # 最小堆为空，需要将当前时间改为队列最近的进入队列时间，以便能将任务从队列中加入最小堆
                curTime = max(curTime, tasks[i][0])
            while i < n and curTime >= tasks[i][0]:  # 当前时间大于任务的进入队列时间，需要将任务提取到最小堆中
                heap.insert((tasks[i][1], i))  # 进入最小堆为元组(运行时间,索引)
                i += 1
            task = heap.extractMin()
            curTime += task[0]
            ans.append(task[1])
        while not heap.isEmpty():
            ans.append(heap.extractMin()[1])
        return ans


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    # 向堆中插入值
    def insert(self, item):
        self.heap.append(item)
        i = self.size
        self.size += 1
        while i > 0 and (self.heap[self.parent(i)][0] > item[0]
                         or self.heap[self.parent(i)][0] == item[0] and self.heap[self.parent(i)][1] > item[1]):  # 将小于父节点的值向上提升
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
        if left < self.size and (self.heap[left][0] < self.heap[minIndex][0]
                                 or self.heap[left][0] == self.heap[minIndex][0] and self.heap[left][1] < self.heap[minIndex][1]):
            minIndex = left
        if right < self.size and (self.heap[right][0] < self.heap[minIndex][0]
                                  or self.heap[right][0] == self.heap[minIndex][0] and self.heap[right][1] < self.heap[minIndex][1]):
            minIndex = right
        if minIndex != i:
            self.heap[minIndex], self.heap[i] = self.heap[i], self.heap[minIndex]
            self.minHeapify(minIndex)  # 交换后子节点可能不满足最小堆性质，需要递归向下执行

    # 求父节点的索引
    def parent(self, i):
        return (i - 1) // 2

    def isEmpty(self):
        return self.size == 0


s = Solution()
print(s.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
print(s.getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))

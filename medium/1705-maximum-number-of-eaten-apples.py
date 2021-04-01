'''
吃苹果的最大数目
有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，
这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。

你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。

给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。

提示：

apples.length == n
days.length == n
1 <= n <= 2 * 10^4
0 <= apples[i], days[i] <= 2 * 10^4
只有在 apples[i] = 0 时，days[i] = 0 才成立

'''
from typing import List
'''
思路：优先队列。
遍历输入数组，将其加入优先队列，每次都吃最近要过期的苹果。
用最小堆当作优先队列。
时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        count = 0
        day = 0
        heap = MinHeap()
        while day < n or heap.notEmpty():
            if day < n and apples[day] > 0:
                heap.insert([days[day] + day, apples[day]])  # 将 [过期日，苹果数] 加入队列
            # 从队列中提取可以吃的苹果，吃掉一个
            while heap.notEmpty():
                apple = heap.getMin()
                if apple[0] > day:  # 当前天从0开始，所以存储在队列中的过期日必须大于当前天
                    apple[1] -= 1
                    count += 1
                    if apple[1] == 0:  # 苹果已经吃完，扔掉
                        heap.extractMin()
                    break
                else:
                    heap.extractMin()  # 过期苹果扔掉
            day += 1
        return count


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


s = Solution()
print(s.eatenApples([2, 1, 10], [2, 10, 1]))
print(s.eatenApples(apples=[20000], days=[20000]))
print(s.eatenApples(apples=[1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2]))
print(s.eatenApples(apples=[3, 0, 0, 0, 0, 2], days=[3, 0, 0, 0, 0, 2]))

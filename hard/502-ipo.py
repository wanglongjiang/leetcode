'''
IPO
假设 力扣（LeetCode）即将开始其 IPO。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。
由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。

给定若干个项目。对于每个项目 i，它都有一个纯利润 Pi，并且需要最小的资本 Ci 来启动相应的项目。最初，你有 W 资本。
当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

总而言之，从给定项目中选择最多 k 个不同项目的列表，以最大化最终资本，并输出最终可获得的最多资本。

提示：

假设所有输入数字都是非负整数。
表示利润和资本的数组的长度不超过 50000。
答案保证在 32 位有符号整数范围内。
'''
from typing import List
'''
思路：排序+最大堆
每减少一次k，需要从<=当前资本w的项目中找到利润最大的项目i，将其利润加到w上。
主要算法是：
1、按照资本从小到大排序所有项目
2、将<=当前资本的项目利润p加入最大堆，然后从最大堆中选择1个最大利润p，将w加上p:w=p+w
3、重复上面过程2 ，执行k次
时间复杂度：O(nlogn)
空间复杂度：O(n)
'''


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        li = sorted(zip(profits, capital), key=lambda x: x[1])
        n = len(li)
        heap = MaxHeap()
        i = 0
        for _ in range(k):
            while i < n and li[i][1] <= w:  # 取出所有成本<=w的项目
                heap.insert(li[i][0])  # 将利润值插入堆
                i += 1
            if heap.notEmpty():
                w += heap.extractMax()
            else:
                break
        return w


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    # 向堆中插入值
    def insert(self, item):
        self.heap.append(item)
        i = self.size
        self.size += 1
        while i > 0 and self.heap[self.parent(i)] < item:  # 将大于父节点的值向上提升
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # 从堆中删除最大元素并返回
    def extractMax(self):
        i = self.heap[0]
        self.size -= 1
        last = self.heap.pop()
        if self.size:
            self.heap[0] = last
        self.maxHeapify(0)
        return i

    # 保持最大堆的性质
    def maxHeapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minIndex = i
        # 如果左、右子节点大于父节点，不满足最大堆性质，需要将父节点与左或右节点交换，使之满足最大堆性质
        if left < self.size and self.heap[left] > self.heap[minIndex]:
            minIndex = left
        if right < self.size and self.heap[right] > self.heap[minIndex]:
            minIndex = right
        if minIndex != i:
            self.heap[minIndex], self.heap[i] = self.heap[i], self.heap[minIndex]
            self.maxHeapify(minIndex)  # 交换后子节点可能不满足最大堆性质，需要递归向下执行

    # 求父节点的索引
    def parent(self, i):
        return (i - 1) // 2

    def getMax(self):
        return self.heap[0]

    def notEmpty(self):
        return self.size > 0


s = Solution()
print(s.findMaximizedCapital(10, 0, [1, 2, 3], [0, 1, 2]))
print(s.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))

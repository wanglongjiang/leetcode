'''
积压订单中的订单总数

给你一个二维整数数组 orders ，其中每个 orders[i] = [pricei, amounti, orderTypei] 表示有 amounti 笔类型为 orderTypei 、
价格为 pricei 的订单。

订单类型 orderTypei 可以分为两种：

0 表示这是一批采购订单 buy
1 表示这是一批销售订单 sell
注意，orders[i] 表示一批共计 amounti 笔的独立订单，这些订单的价格和类型相同。对于所有有效的 i ，
由 orders[i] 表示的所有订单提交时间均早于 orders[i+1] 表示的所有订单。

存在由未执行订单组成的 积压订单 。积压订单最初是空的。提交订单时，会发生以下情况：

如果该订单是一笔采购订单 buy ，则可以查看积压订单中价格 最低 的销售订单 sell 。
如果该销售订单 sell 的价格 低于或等于 当前采购订单 buy 的价格，则匹配并执行这两笔订单，
并将销售订单 sell 从积压订单中删除。否则，采购订单 buy 将会添加到积压订单中。
反之亦然，如果该订单是一笔销售订单 sell ，则可以查看积压订单中价格 最高 的采购订单 buy 。
如果该采购订单 buy 的价格 高于或等于 当前销售订单 sell 的价格，则匹配并执行这两笔订单，并将采购订单 buy 从积压订单中删除。
否则，销售订单 sell 将会添加到积压订单中。
输入所有订单后，返回积压订单中的 订单总数 。由于数字可能很大，所以需要返回对 109 + 7 取余的结果。

1 <= orders.length <= 10^5
orders[i].length == 3
1 <= pricei, amounti <= 10^9
orderTypei 为 0 或 1
'''
from typing import List
'''
思路1、堆。构造采购订单的最大堆，销售订单的最小堆。
    遍历订单list
    1、遇到采购订单，先在销售订单堆里面查找，如果最小堆里没有满足需求的订单，将采购订单加入最大堆。
    2、遇到销售订单，先在采购订单堆里面查找，如果最大堆里没有满足需求的订单，将销售订单加入最小堆。
    所有的订单都处理完之后，返回2个堆中订单数之和
时间复杂度：最坏情况下O(nlogn)，这种情况下所有订单都入堆。10^6。
空间复杂度：最坏情况下O(n)
'''


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyOrders, sellOrders = MaxHeap(), MinHeap()  # 采购是最大堆，销售是最小堆
        for order in orders:
            if order[2] == 0:  # 当前订单为采购订单，需要从销售订单里面查找最小值
                while sellOrders.notEmpty() and sellOrders.getMin()[0] <= order[0]:  # 如果价格最低的销售订单小于等于当前采购订单价格，执行订单
                    sellOrder = sellOrders.getMin()
                    if sellOrder[1] < order[1]:  # 订单数量大于当前销售订单数量，需要删除当前销售订单，当前订单数量减去销售订单数量
                        order[1] -= sellOrder[1]
                        sellOrders.extractMin()
                    elif sellOrder[1] > order[1]:  # 销售订单数量大于当前订单数量，当前订单处理完毕，销售订单减去数量
                        sellOrder[1] -= order[1]
                        order[1] = 0
                        break
                    else:  # 当前订单数等于销售订单数，需要删除销售订单,当前订单处理完成
                        sellOrders.extractMin()
                        order[1] = 0
                        break
                if order[1] > 0:  # 当前订单未处理完毕，需要加入采购订单
                    buyOrders.insert(order)
            else:  # 当前订单为销售订单，需要从采购订单里面查找最大值，基本与上面的采购订单逻辑互为镜像
                while buyOrders.notEmpty() and buyOrders.getMax()[0] >= order[0]:  # 如果价格最高的采购订单大于等于当前销售订单价格，执行订单
                    buyOrder = buyOrders.getMax()
                    if buyOrder[1] < order[1]:  # 订单数量大于当前采购订单数量，需要删除当前采购订单，当前订单数量减去采购订单数量
                        order[1] -= buyOrder[1]
                        buyOrders.extractMin()
                    elif buyOrder[1] > order[1]:  # 采购订单数量大于当前订单数量，当前订单处理完毕，采购订单减去数量
                        buyOrder[1] -= order[1]
                        order[1] = 0
                        break
                    else:  # 当前订单数等于采购订单数，需要删除采购订单,当前订单处理完成
                        buyOrders.extractMin()
                        order[1] = 0
                        break
                if order[1] > 0:  # 当前订单未处理完毕，需要加入销售订单
                    sellOrders.insert(order)
        # 所有的订单都处理完成之后，统计剩余的订单数
        ans = sum([item[1] for item in buyOrders.heap])
        ans += sum([item[1] for item in sellOrders.heap])
        return ans % (10**9 + 7)


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    # 向堆中插入值
    def insert(self, item):
        self.heap.append(item)
        i = self.size
        self.size += 1
        while i > 0 and self.heap[self.parent(i)][0] < item[0]:  # 将大于父节点的值向上提升
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # 从堆中删除最大元素并返回
    def extractMin(self):
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
        if left < self.size and self.heap[left][0] > self.heap[minIndex][0]:
            minIndex = left
        if right < self.size and self.heap[right][0] > self.heap[minIndex][0]:
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
print(s.getNumberOfBacklogOrders([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]))
print(s.getNumberOfBacklogOrders([[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]))

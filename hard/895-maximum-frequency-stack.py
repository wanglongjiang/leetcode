'''
最大频率栈

实现 FreqStack，模拟类似栈的数据结构的操作的一个类。

FreqStack 有两个函数：

push(int x)，将整数 x 推入栈中。
pop()，它移除并返回栈中出现最频繁的元素。
如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。
 

示例：

输入：
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
输出：[null,null,null,null,null,null,null,5,7,5,4]
解释：
执行六次 .push 操作后，栈自底向上为 [5,7,5,7,4,5]。然后：

pop() -> 返回 5，因为 5 是出现频率最高的。
栈变成 [5,7,5,7,4]。

pop() -> 返回 7，因为 5 和 7 都是频率最高的，但 7 最接近栈顶。
栈变成 [5,7,5,4]。

pop() -> 返回 5 。
栈变成 [5,7,4]。

pop() -> 返回 4 。
栈变成 [5,7]。
 

提示：

对 FreqStack.push(int x) 的调用中 0 <= x <= 10^9。
如果栈的元素数目为零，则保证不会调用  FreqStack.pop()。
单个测试样例中，对 FreqStack.push 的总调用次数不会超过 10000。
单个测试样例中，对 FreqStack.pop 的总调用次数不会超过 10000。
所有测试样例中，对 FreqStack.push 和 FreqStack.pop 的总调用次数不会超过 150000。
'''
'''
思路：堆
使用最大堆，堆中每个元素保存数值和它出现的次数，比较2个元素首先比较出现频率，频率相同的再比较入堆顺序
时间复杂度：push、pop都是O(logn)
'''


class FreqStack:
    def __init__(self):
        self.heap = MaxHeap()

    def push(self, val: int) -> None:
        self.heap.insert(val)

    def pop(self) -> int:
        return self.heap.extractMax()


# 堆节点
class HeapNode:
    def __init__(self, val, order):
        self.val = val  # 值
        self.count = 1  # 出现频率
        self.order = order  # 排序


# 定义最大堆
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.indexMap = {}
        self.size = 0
        self.order = 0

    # 比较2个节点，先比较频率，频率相同的比较排序
    def isBigger(self, node1, node2):
        return node1.count > node2.count or (node1.count == node2.count and node1.order > node2.order)

    # 向堆中插入值
    def insert(self, val):
        if val in self.indexMap:  # 数据已存在，更新原先的节点的频率
            i = self.indexMap[val]
            self.heap[i].count += 1
            while i > 0 and self.isBigger(self.heap[i], self.heap[self.parent(i)]):  # 频率大于父节点，或者排序大于父节点，需要提升
                parentIdx = self.parent(i)
                parentVal = self.heap[parentIdx].val
                self.indexMap[val], self.indexMap[parentVal] = self.indexMap[parentVal], self.indexMap[val]
                self.heap[i], self.heap[parentIdx] = self.heap[parentIdx], self.heap[i]
                i = parentIdx
        else:  # 数据不存在，插入新的节点，新的节点肯定排到最后，堆不需要调整
            self.size += 1
            node = HeapNode(val, self.order)
            self.order += 1
            self.heap.append(node)
            self.indexMap[val] = self.size - 1

    # 从堆中提取最大元素
    def extractMax(self):
        node = self.heap[0]
        val = node.val
        if node.count > 1:  # 多于1个，不需要删除节点，调整其频率
            node.count -= 1
        else:  # 等于1个，删除节点
            del self.indexMap[val]
            self.size -= 1
            last = self.heap.pop()
            if self.size:
                self.heap[0] = last
        self.maxHeapify(0)
        return val

    # 保持最大堆的性质
    def maxHeapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        maxIndex = i
        # 如果左、右子节点大于父节点，不满足最大堆性质，需要将父节点与左或右节点交换，使之满足最大堆性质
        if left < self.size and self.isBigger(self.heap[left], self.heap[maxIndex]):
            maxIndex = left
        if right < self.size and self.isBigger(self.heap[right], self.heap[maxIndex]):
            maxIndex = right
        if maxIndex != i:
            val1, val2 = self.heap[i].val, self.heap[maxIndex].val
            self.indexMap[val1], self.indexMap[val2] = self.indexMap[val1], self.indexMap[val2]
            self.heap[maxIndex], self.heap[i] = self.heap[i], self.heap[maxIndex]
            self.maxHeapify(maxIndex)  # 交换后子节点可能不满足最大堆性质，需要递归向下执行

    # 求父节点的索引
    def parent(self, i):
        return (i - 1) // 2


s = FreqStack()
s.push(5)
s.push(7)
s.push(5)
s.push(7)
s.push(4)
s.push(5)

print(s.pop() == 5)
print(s.pop() == 7)
print(s.pop() == 5)
print(s.pop() == 4)

'''
面试题 03.05. 栈排序
栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，
但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。

示例1:

 输入：
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
 输出：
[null,null,null,1,null,2]
示例2:

输入：
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
 输出：
[null,null,null,null,null,true]
说明:

栈中的元素数目在[0, 5000]范围内。
'''
'''
思路：堆
这不就是最小堆嘛

时间复杂度：
push、pop都是O(logn)
peek、isEmpty是O(1)
'''


class SortedStack:
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[(i - 1) // 2] > self.heap[i]:
            parent = (i - 1) // 2
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def pop(self) -> None:
        if not self.heap:
            return
        num = self.heap.pop()
        if not self.heap:
            return
        self.heap[0] = num
        self.minHeapify(0)

    def peek(self) -> int:
        if not self.heap:
            return -1
        return self.heap[0]

    def isEmpty(self) -> bool:
        return not self.heap

    def minHeapify(self, i):
        left, right = i * 2 + 1, i * 2 + 2
        minIdx = i
        if left < len(self.heap) and self.heap[minIdx] > self.heap[left]:
            minIdx = left
        if right < len(self.heap) and self.heap[minIdx] > self.heap[right]:
            minIdx = right
        if minIdx != i:
            self.heap[i], self.heap[minIdx] = self.heap[minIdx], self.heap[i]
            self.minHeapify(minIdx)


s = SortedStack()
print(s.peek())
print(s.peek())
print(s.pop())
print(s.isEmpty())
print(s.peek())
print(s.push(40))
print(s.pop())
print(s.push(19))
print(s.push(44))
print(s.pop())
print(s.pop())
print(s.push(42))
print(s.isEmpty())
print(s.push(8))
print(s.push(29))
print(s.push(25))
print(s.isEmpty())
print(s.peek())
print(s.isEmpty())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.push(52))
print(s.push(63))

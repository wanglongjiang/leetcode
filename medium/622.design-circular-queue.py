'''
设计循环队列

设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
 

示例：

MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
 

提示：

所有的值都在 0 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。
'''
'''
思路：数组
用循环数组实现循环队列，2个指针front,last分别指向队列头部元素和队尾元素第1个空位
用size保存当前队列中元素数量

与641.[设计循环双端队列](medium/641-design-circular-deque.py)类似

时间复杂度：所有操作都是O(n)
空间复杂度：O(n)
'''


class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.limit = k
        self.front = 0  # front指针指向当前元素
        self.last = 0  # last指针指向下一个空位
        self.data = [0] * self.limit

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.last] = value
        if self.last == self.limit - 1:
            self.last = 0
        else:
            self.last += 1
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.limit - 1:
            self.front = 0
        else:
            self.front += 1
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.last - 1]  # last指向下一个空位，所以上一个为队尾元素

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit

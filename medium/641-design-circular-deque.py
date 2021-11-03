'''
设计循环双端队列
设计实现双端队列。
你的实现需要支持以下操作：

MyCircularDeque(k)：构造函数,双端队列的大小为k。
insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。
示例：

MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4
 
 

提示：

所有值的范围为 [1, 1000]
操作次数的范围为 [1, 1000]
请不要使用内置的双端队列库。

'''
'''
思路：数组
用循环数组实现双向队列，2个指针front,last分别指向队列头部元素和队尾元素第1个空位
用size保存当前队列中元素数量

与621.[设计循环队列](medium/621.design-circular-queue.py)类似

时间复杂度：所有操作都是O(n)
空间复杂度：O(n)
'''


class MyCircularDeque:
    def __init__(self, k: int):
        self.size = 0
        self.limit = k
        self.front = 0  # front指针指向当前元素
        self.last = 0  # last指针指向下一个空位
        self.data = [0] * self.limit

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.front == 0:
            self.front = self.limit - 1
        else:
            self.front -= 1
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.last] = value
        if self.last == self.limit - 1:
            self.last = 0
        else:
            self.last += 1
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.limit - 1:
            self.front = 0
        else:
            self.front += 1
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.last == 0:
            self.last = self.limit - 1
        else:
            self.last -= 1
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.last - 1]  # last指向下一个空位，所以上一个为队尾元素

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit


s = MyCircularDeque(4)
s.insertFront(9)
s.deleteLast()
print(s.getRear())
print(s.getFront())
'''
["MyCircularDeque","insertFront","deleteLast","getRear","getFront","getFront","deleteFront","insertFront","insertLast","insertFront","getFront","insertFront"]
[[4],[9],[],[],[],[],[],[6],[5],[9],[],[6]]

[null,true,true,-1,-1,-1,false,true,true,true,9,true] # TODO
'''

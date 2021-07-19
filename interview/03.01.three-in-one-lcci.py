'''
面试题 03.01. 三合一
三合一。描述如何只用一个数组来实现三个栈。

你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。

构造函数会传入一个stackSize参数，代表每个栈的大小。

示例1:

 输入：
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
 输出：
[null, null, null, 1, -1, -1, true]
说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
示例2:

 输入：
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
 输出：
[null, null, null, null, 2, 1, -1, -1]
'''
'''
思路：数组
设一个大小为3*stackSize的指针
维护3个指针，分别指向数组的0，1/3,2/3处
当执行入栈操作，将指针指向的位置设置为value，然后指针向高位移动一步
当执行入栈操作，将指针向低位移动一步，返回原指针指向的元素

'''


class TripleInOne:
    def __init__(self, stackSize: int):
        self.p = [0, stackSize, stackSize * 2]
        self.elements = [0] * 3 * stackSize
        self.stckSize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self.p[stackNum] == self.stckSize * (stackNum + 1):  # 栈已满
            return
        self.elements[self.p[stackNum]] = value
        self.p[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if self.p[stackNum] == self.stckSize * stackNum:  # 栈为空
            return -1
        self.p[stackNum] -= 1
        return self.elements[self.p[stackNum]]

    def peek(self, stackNum: int) -> int:
        if self.p[stackNum] == self.stckSize * stackNum:  # 栈为空
            return -1
        return self.elements[self.p[stackNum] - 1]

    def isEmpty(self, stackNum: int) -> bool:
        return self.p[stackNum] == self.stckSize * stackNum

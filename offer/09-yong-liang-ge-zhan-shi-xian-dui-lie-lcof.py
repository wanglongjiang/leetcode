'''
剑指 Offer 09. 用两个栈实现队列

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
'''
'''
思路：栈
设2个栈inStk和outStk
appendTail操作，执行inStk.push，时间复杂度：O(1)
deleteHead操作，如果outStk不为空，执行outStk.pop，如果outStk为空，将inStk中的所有元素进行出栈，push到outStck中

'''


class CQueue:
    def __init__(self):
        self.inStack, self.outStack = [], []

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        if self.outStack:
            return self.outStack.pop()
        elif self.inStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            return self.outStack.pop()
        return -1

'''
面试题 03.02. 栈的最小值
请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。


示例：

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''
'''
思路：双栈
用2个栈，dataStack执行常规的数据出入栈操作
minStack，当入栈时，对比x与栈顶元素，如果x比栈顶元素大，栈顶元素再次入栈，否则将x入栈

时间复杂度：3个操作都是O(1)
'''


class MinStack:
    def __init__(self):
        self.dataStack, self.minStack = [], [float('inf')]

    def push(self, x: int) -> None:
        self.dataStack.append(x)
        if self.minStack[-1] > x:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.dataStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.dataStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

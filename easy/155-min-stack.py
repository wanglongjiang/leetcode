'''
最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

提示：
pop、top 和 getMin 操作总是在 非空栈 上调用。

'''
'''
思路：双栈
2个栈，1个栈stack保存正常的数据，另外一个minStack栈保存当前数据入栈后的最小值。
核心就在于minStack，执行push操作时，当minStack栈顶元素大于x，则minstack入栈x，否则入栈minStack栈顶元素
执行pop操作时，当前栈对应的最小元素会因为这种设计也保持正确

4个操作的时间复杂度都是O(1)
'''


class MinStack:
    def __init__(self):
        self.minStack, self.stack = [float('inf')], []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x > self.minStack[-1]:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

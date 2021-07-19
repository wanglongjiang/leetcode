'''
剑指 Offer 30. 包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次
 

注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
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

    def min(self) -> int:
        return self.minStack[-1]

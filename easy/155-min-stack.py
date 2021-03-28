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
思路：栈
pop可能会有查找最小元素，时间复杂度O(n)
push，只需要对比最小元素是否发生变化，时间复杂度为O(1)
top直接取栈顶，时间复杂度：O(1)
getMin直接取最小堆的第1个元素，时间复杂度：O(1)
'''


class MinStack:
    def __init__(self):
        self.stack = []
        self.minItem = float('inf')

    def push(self, val: int) -> None:
        if val > self.minItem:
            self.minItem = val
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minItem:
            self.minItem = min(self.stack) if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minItem

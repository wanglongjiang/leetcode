'''
面试题 03.04. 化栈为队
实现一个MyQueue类，该类用两个栈来实现一个队列。


示例：

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

说明：

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
'''
'''
思路：双栈模拟队列
设2个栈，1个inStk，1个outStk
push操作会执行inStk的push；
pop操作会执行outStk的pop，如果outStk为空，需要将inStk内的元素pop到outStk内
peek操作类似于pop
'''


class MyQueue:
    def __init__(self):
        self.inStk, self.outStk = [], []

    def push(self, x: int) -> None:
        self.inStk.append(x)

    def pop(self) -> int:
        if self.outStk:
            return self.outStk.pop()
        while self.inStk:
            self.outStk.append(self.inStk.pop())
        if self.outStk:
            return self.outStk.pop()

    def peek(self) -> int:
        if self.outStk:
            return self.outStk[-1]
        while self.inStk:
            self.outStk.append(self.inStk.pop())
        if self.outStk:
            return self.outStk[-1]

    def empty(self) -> bool:
        return not self.inStk and not self.outStk

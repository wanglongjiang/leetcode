'''
716. 最大栈
设计一个最大栈数据结构，既支持栈操作，又支持查找栈中最大元素。

实现 MaxStack 类：

MaxStack() 初始化栈对象
void push(int x) 将元素 x 压入栈中。
int pop() 移除栈顶元素并返回这个元素。
int top() 返回栈顶元素，无需移除。
int peekMax() 检索并返回栈中最大元素，无需移除。
int popMax() 检索并返回栈中最大元素，并将其移除。如果有多个最大元素，只要移除 最靠近栈顶 的那个。


示例：

输入
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
输出
[null, null, null, null, 5, 5, 1, 5, 1, 5]

解释
MaxStack stk = new MaxStack();
stk.push(5);   // [5] - 5 既是栈顶元素，也是最大元素
stk.push(1);   // [5, 1] - 栈顶元素是 1，最大元素是 5
stk.push(5);   // [5, 1, 5] - 5 既是栈顶元素，也是最大元素
stk.top();     // 返回 5，[5, 1, 5] - 栈没有改变
stk.popMax();  // 返回 5，[5, 1] - 栈发生改变，栈顶元素不再是最大元素
stk.top();     // 返回 1，[5, 1] - 栈没有改变
stk.peekMax(); // 返回 5，[5, 1] - 栈没有改变
stk.pop();     // 返回 1，[5] - 此操作后，5 既是栈顶元素，也是最大元素
stk.top();     // 返回 5，[5] - 栈没有改变


提示：

-107 <= x <= 107
最多调用 104 次 push、pop、top、peekMax 和 popMax
调用 pop、top、peekMax 或 popMax 时，栈中 至少存在一个元素

进阶

试着设计解决方案：调用 top 方法的时间复杂度为 O(1) ，调用其他方法的时间复杂度为 O(logn) 。
'''
'''
思路：双栈
设2个栈，一个栈存放正常的出入栈数据，
另外一个栈存放递增数据，保持栈顶数据最大，入栈时，只有当前值大于等于栈顶元素才入栈，出栈时只有另外一个栈的出栈数值等于最大栈的元素，最大栈才出栈
时间复杂度：O(n)
空间复杂度：O(n)

'''


class MaxStack:
    def __init__(self):
        self.stk, self.maxStk = [], []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.maxStk or x >= self.maxStk[-1]:
            self.maxStk.append(x)

    def pop(self) -> int:
        if self.maxStk and self.stk[-1] == self.maxStk[-1]:
            self.maxStk.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def peekMax(self) -> int:
        return self.maxStk[-1]

    def popMax(self) -> int:
        val = self.maxStk.pop()
        tmp = []
        while self.stk[-1] != val:
            tmp.append(self.stk.pop())
        self.stk.pop()
        while tmp:
            self.stk.append(tmp.pop())
        return val


stk = MaxStack()
print(stk.push(5))  # [5] - 5 既是栈顶元素，也是最大元素
print(stk.push(1))  # [5, 1] - 栈顶元素是 1，最大元素是 5
print(stk.push(5))  # [5, 1, 5] - 5 既是栈顶元素，也是最大元素
print(stk.top())  # 返回 5，[5, 1, 5] - 栈没有改变
print(stk.popMax())  # 返回 5，[5, 1] - 栈发生改变，栈顶元素不再是最大元素
print(stk.top())  # 返回 1，[5, 1] - 栈没有改变
print(stk.peekMax())  # 返回 5，[5, 1] - 栈没有改变
print(stk.pop())  # 返回 1，[5] - 此操作后，5 既是栈顶元素，也是最大元素
print(stk.top())  # 返回 5，[5] - 栈没有改变

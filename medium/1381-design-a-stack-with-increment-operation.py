'''
设计一个支持增量操作的栈

请你设计一个支持下述操作的栈。

实现自定义栈类 CustomStack ：

CustomStack(int maxSize)：用 maxSize 初始化对象，maxSize 是栈中最多能容纳的元素数量，栈在增长到 maxSize 之后
则不支持 push 操作。
void push(int x)：如果栈还未增长到 maxSize ，就将 x 添加到栈顶。
int pop()：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 -1 。
void inc(int k, int val)：栈底的 k 个元素的值都增加 val 。如果栈中元素总数小于 k ，则栈中的所有元素都增加 val 。

提示：

1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
每种方法 increment，push 以及 pop 分别最多调用 1000 次
'''
'''
思路：差分数组
从栈顶到栈底存储为差分数组，各函数主要逻辑如下：
push(a)，需要将当前栈顶元素修改为与a的差，然后a入栈
pop()，栈顶元素a出栈，然后将新的栈顶元素恢复成实际值
inc()，从栈底开始的第k个元素+val，如果k>len(stack)，将栈顶元素+val

时间复杂度：push、pop、inc都是O(1)
'''


class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.nums = []

    def push(self, x: int) -> None:
        if len(self.nums) == self.maxSize:
            return
        if not self.nums:
            self.nums.append(x)
        else:
            self.nums[-1] = self.nums[-1] - x
            self.nums.append(x)

    def pop(self) -> int:
        if not self.nums:
            return -1
        x = self.nums.pop()
        if self.nums:
            self.nums[-1] += x
        return x

    def increment(self, k: int, val: int) -> None:
        if not self.nums:
            return
        if len(self.nums) >= k:
            self.nums[k - 1] += val
        else:
            self.nums[-1] += val


customStack = CustomStack(3)  # 栈是空的 []
customStack.push(1)  # 栈变为 [1]
customStack.push(2)  # 栈变为 [1, 2]
print(customStack.pop())  # 返回 2 --> 返回栈顶值 2，栈变为 [1]
customStack.push(2)  # 栈变为 [1, 2]
customStack.push(3)  # 栈变为 [1, 2, 3]
customStack.push(4)  # 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
customStack.increment(5, 100)  # 栈变为 [101, 102, 103]
customStack.increment(2, 100)  # 栈变为 [201, 202, 103]
print(customStack.pop())  # 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
print(customStack.pop())  # 返回 202 --> 返回栈顶值 202，栈变为 [201]
print(customStack.pop())  # 返回 201 --> 返回栈顶值 201，栈变为 []
print(customStack.pop())
'''
面试题 03.03. 堆盘子
堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。
请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。
此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。
进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。

当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1.

示例1:

 输入：
["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
[[1], [1], [2], [1], [], []]
 输出：
[null, null, null, 2, 1, -1]
示例2:

 输入：
["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
[[2], [1], [2], [3], [0], [0], [0]]
 输出：
[null, null, null, null, 2, 1, 3]
'''
'''
思路：栈、数组
设一个数组，数组内元素为栈
执行push、pop操作，针对数组最后一个栈进行，如果pop操作后栈为空，删除
popAt针对指定的元素，如果popAt操作后栈为空，删除
'''


class StackOfPlates:
    def __init__(self, cap: int):
        self.cap = cap
        self.stks = []

    def push(self, val: int) -> None:
        if not self.stks or len(self.stks[-1]) == self.cap:
            self.stks.append([])
        self.stks[-1].append(val)

    def pop(self) -> int:
        ans = -1
        if self.stks:
            ans = self.stks[-1].pop()
            if not self.stks[-1]:
                self.stks.pop()
        return ans

    def popAt(self, index: int) -> int:
        ans = -1
        if len(self.stks) > index:
            ans = self.stks[index].pop()
            if not self.stks[index]:
                del self.stks[index]
        return ans

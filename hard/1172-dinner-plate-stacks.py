'''
餐盘栈
我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。

实现一个叫「餐盘」的类 DinnerPlates：

DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
 
提示：

1 <= capacity <= 20000
1 <= val <= 20000
0 <= index <= 100000
最多会对 push，pop，和 popAtStack 进行 200000 次调用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dinner-plate-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from sortedcontainers import SortedDict
'''
思路：有序集合
设有序集合full，保存已经满的栈，key为栈编号，val为栈
设有序集合half，保存不满的栈，key为栈编号，val为栈
设有序集合empty，保存空栈
1. 执行push操作，
> 先在empty和half中找编号最小的未满栈，如果能找到，数据入栈，数据入栈后如果满了，需要移动到full中
> 如果在half中没有未满栈，创建新的栈，数据入栈，栈加入half中

2. 执行pop操作，
> 在full和half中找到编号最大的栈，执行出栈。
> 数据出栈后，如果栈不满，需要移动到half中，如果栈为空需要移动到empty中。

3. 执行popAtStack操作
> 在full,half,empty中寻找指定的栈，执行出栈。
> 数据出栈后，如果栈不满，需要移动到half中，如果栈为空需要移动到empty中。

'''


class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stkno = 0
        self.empty, self.full, self.half = SortedDict(), SortedDict(), SortedDict()

    def push(self, val: int) -> None:
        if self.empty or self.half:
            if self.empty and self.half:  # empty和half均不为空
                if self.empty.keys()[0] < self.half.keys()[0]:  # 最小的栈在empty中
                    key = self.empty.keys()[0]
                    stk = self.empty[key]
                    stk.append(val)
                    del self.empty[key]
                    if len(stk) == self.capacity:
                        self.full[key] = stk
                    else:
                        self.half[key] = stk
                else:  # 最小的栈在half中
                    key = self.half.keys()[0]
                    stk = self.half[key]
                    stk.append(val)
                    if len(stk) == self.capacity:
                        del self.half[key]
                        self.full[key] = stk
            elif self.empty:
                key = self.empty.keys()[0]
                stk = self.empty[key]
                stk.append(val)
                if len(stk) == self.capacity:
                    del self.empty[key]
                    self.full[key] = stk
                else:
                    del self.empty[key]
                    self.half[key] = stk
            else:
                key = self.half.keys()[0]
                stk = self.half[key]
                stk.append(val)
                if len(stk) == self.capacity:
                    del self.half[key]
                    self.full[key] = stk
        else:  # empty和half均为空，需要创建新的栈
            stk = []
            stk.append(val)
            if len(stk) == self.capacity:
                self.full[self.stkno] = stk
            else:
                self.half[self.stkno] = stk
            self.stkno += 1

    def pop(self) -> int:
        if self.full or self.half:
            if self.full and self.half:
                if self.full.keys()[-1] > self.half.keys()[-1]:  # full中的栈编号更大
                    key = self.full.keys()[-1]
                    stk = self.full[key]
                    val = stk.pop()
                    del self.full[key]
                    if not stk:
                        self.empty[key] = stk
                    else:
                        self.half[key] = stk
                    return val
                else:  # half中的编号更大
                    key = self.half.keys()[-1]
                    stk = self.half[key]
                    val = stk.pop()
                    if not stk:
                        del self.half[key]
                        self.empty[key] = stk
                    return val
            elif self.full:  # full不为空
                key = self.full.keys()[-1]
                stk = self.full[key]
                val = stk.pop()
                del self.full[key]
                if not stk:
                    self.empty[key] = stk
                else:
                    self.half[key] = stk
                return val
            else:  # half不为空
                key = self.half.keys()[-1]
                stk = self.half[key]
                val = stk.pop()
                if not stk:
                    del self.half[key]
                    self.empty[key] = stk
                return val
        else:  # 所有的栈均为空
            return -1

    def popAtStack(self, index: int) -> int:
        if index in self.full:
            stk = self.full[index]
            val = stk.pop()
            del self.full[index]
            if not stk:
                self.empty[index] = stk
            else:
                self.half[index] = stk
            return val
        elif index in self.half:
            stk = self.half[index]
            val = stk.pop()
            if not stk:
                del self.half[index]
                self.empty[index] = stk
            return val
        else:
            return -1


s = DinnerPlates(2)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.popAtStack(0))
s.push(20)
s.push(21)
print(s.popAtStack(1))
print(s.popAtStack(1) == 3)
print(s.pop() == 21)
print(s.pop() == 5)
print(s.pop() == 20)
print(s.pop() == 1)
print(s.pop() == -1)

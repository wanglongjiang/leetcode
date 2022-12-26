'''
最大频率栈

实现 FreqStack，模拟类似栈的数据结构的操作的一个类。

FreqStack 有两个函数：

push(int x)，将整数 x 推入栈中。
pop()，它移除并返回栈中出现最频繁的元素。
如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。
 

示例：

输入：
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
输出：[null,null,null,null,null,null,null,5,7,5,4]
解释：
执行六次 .push 操作后，栈自底向上为 [5,7,5,7,4,5]。然后：

pop() -> 返回 5，因为 5 是出现频率最高的。
栈变成 [5,7,5,7,4]。

pop() -> 返回 7，因为 5 和 7 都是频率最高的，但 7 最接近栈顶。
栈变成 [5,7,5,4]。

pop() -> 返回 5 。
栈变成 [5,7,4]。

pop() -> 返回 4 。
栈变成 [5,7]。
 

提示：

对 FreqStack.push(int x) 的调用中 0 <= x <= 10^9。
如果栈的元素数目为零，则保证不会调用  FreqStack.pop()。
单个测试样例中，对 FreqStack.push 的总调用次数不会超过 10000。
单个测试样例中，对 FreqStack.pop 的总调用次数不会超过 10000。
所有测试样例中，对 FreqStack.push 和 FreqStack.pop 的总调用次数不会超过 150000。
'''
from sortedcontainers import SortedList
'''
思路：有序集合
设一个有序集合，内部元素为数元组：(-出现频率，入栈的顺序，数值)

入栈的顺序通过维护一个全局变量orderNo，遇到没有出现过的元素将其赋给新的顺序号

还需要维护一个哈希表，key为入栈的val，值为-出现频率

时间复杂度：push、pop都是O(logn)
'''


class FreqStack:
    def __init__(self):
        self.list = SortedList()
        self.orderNo = 0
        self.itemHash = {}

    def push(self, val: int) -> None:
        if val not in self.itemHash:
            self.list.add((-1, self.orderNo, val))
            self.itemHash[val] = -1
        else:
            count = self.itemHash[val]
            self.list.add((count - 1, self.orderNo, val))
            self.itemHash[val] = count - 1
        self.orderNo -= 1  # 因为入栈晚的先出栈，所以后入栈的顺序号需要递减，能够先出栈

    def pop(self) -> int:
        count, _, val = self.list[0]
        if count == -1:
            del self.list[0]
            del self.itemHash[val]
        else:
            del self.list[0]
            self.itemHash[val] = count + 1
        return val


s = FreqStack()
s.push(5)
s.push(7)
s.push(5)
s.push(7)
s.push(4)
s.push(5)

print(s.pop() == 5)
print(s.pop() == 7)
print(s.pop() == 5)
print(s.pop() == 4)

s = FreqStack()
s.push(4)
s.push(0)
s.push(9)
s.push(3)
s.push(4)
s.push(2)
print(s.pop() == 4)
s.push(6)
print(s.pop() == 6)
s.push(1)
print(s.pop() == 1)
s.push(1)
print(s.pop() == 1)
s.push(4)
print(s.pop() == 4)
print(s.pop() == 2)
print(s.pop() == 3)
print(s.pop() == 9)
print(s.pop() == 0)
print(s.pop() == 4)

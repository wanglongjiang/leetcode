'''
剑指 Offer 59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
'''
from collections import deque
'''
思路：单调队列
维护2个队列，第1个队列dataQ，存放push_back传入的数据，pop_front时pop数据
第2个双向队列，maxQ，执行push_back时，将队列中所有<value的元素从队列中删除，然后将val入队
执行pop_front时，如果队列头部的元素maxQ[0]==dataQ[0]，则将dataQ[0]也出队，否则不出队

'''


class MaxQueue:
    def __init__(self):
        self.maxQ, self.dataQ = deque(), deque()

    def max_value(self) -> int:
        if not self.dataQ:
            return -1
        return self.maxQ[0]

    def push_back(self, value: int) -> None:
        self.dataQ.append(value)
        while self.maxQ and self.maxQ[-1] < value:
            self.maxQ.pop()
        self.maxQ.append(value)

    def pop_front(self) -> int:
        if not self.dataQ:
            return -1
        if self.dataQ[0] == self.maxQ[0]:
            self.maxQ.popleft()
        return self.dataQ.popleft()

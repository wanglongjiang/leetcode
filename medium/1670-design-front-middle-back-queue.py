'''
设计前中后队列
请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。

请你完成 FrontMiddleBack 类：

FrontMiddleBack() 初始化队列。
void pushFront(int val) 将 val 添加到队列的 最前面 。
void pushMiddle(int val) 将 val 添加到队列的 正中间 。
void pushBack(int val) 将 val 添加到队里的 最后面 。
int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说：

将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。
从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。
 

示例 1：

输入：
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle",
"popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
输出：
[null, null, null, null, null, 1, 3, 4, 2, -1]

解释：
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // 返回 1 -> [4, 3, 2]
q.popMiddle();    // 返回 3 -> [4, 2]
q.popMiddle();    // 返回 4 -> [2]
q.popBack();      // 返回 2 -> []
q.popFront();     // 返回 -1 -> [] （队列为空）
 

提示：

1 <= val <= 10^9
最多调用 1000 次 pushFront， pushMiddle， pushBack， popFront， popMiddle 和 popBack 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-front-middle-back-queue
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import deque
'''
思路：2个双向队列
用2个双向队列维护，front维护前一半，back维护后一半。

时间复杂度：6个操作均为O(1)
'''


class FrontMiddleBackQueue:
    def __init__(self):
        self.front, self.back = deque(), deque()

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.front) < len(self.back):
            self.front.append(val)
        else:
            self.back.appendleft(val)

    def pushBack(self, val: int) -> None:
        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        self.back.append(val)

    def popFront(self) -> int:
        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        return self.front.popleft() if self.front else -1

    def popMiddle(self) -> int:
        if len(self.front) == len(self.back):
            return self.front.pop() if self.front else -1
        return self.back.popleft() if self.back else -1

    def popBack(self) -> int:
        if self.front and len(self.front) == len(self.back):
            self.back.appendleft(self.front.pop())
        return self.back.pop() if self.back else -1

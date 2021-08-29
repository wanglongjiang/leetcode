'''
346. 数据流中的移动平均值
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。

实现 MovingAverage 类：

MovingAverage(int size) 用窗口大小 size 初始化对象。
double next(int val) 计算并返回数据流中最后 size 个值的移动平均值。


示例：

输入：
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
输出：
[null, 1.0, 5.5, 4.66667, 6.0]

解释：
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // 返回 1.0 = 1 / 1
movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3


提示：

1 <= size <= 1000
-10^5 <= val <= 10^5
最多调用 next 方法 104 次
'''
from collections import deque
'''
思路：队列
初始化2个变量，queue和s，分布保存最后size个数和0
执行next时，s减去队列溢出的数，加上新的数，求平均值

时间复杂度：O(1)
空间复杂度：O(size)
'''


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.s = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.s += val
        if len(self.queue) > self.size:
            self.s -= self.queue.popleft()
        return self.s / len(self.queue)


s = MovingAverage(3)
print(s.next(1))
print(s.next(10))
print(s.next(3))
print(s.next(5))

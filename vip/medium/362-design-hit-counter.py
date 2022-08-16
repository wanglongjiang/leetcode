'''
362. 敲击计数器
设计一个敲击计数器，使它可以统计在过去5分钟内被敲击次数。

每个函数会接收一个时间戳参数（以秒为单位），你可以假设最早的时间戳从1开始，且都是按照时间顺序对系统进行调用（即时间戳是单调递增）。

在同一时刻有可能会有多次敲击。

示例:

HitCounter counter = new HitCounter();

// 在时刻 1 敲击一次。
counter.hit(1);

// 在时刻 2 敲击一次。
counter.hit(2);

// 在时刻 3 敲击一次。
counter.hit(3);

// 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
counter.getHits(4);

// 在时刻 300 敲击一次。
counter.hit(300);

// 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
counter.getHits(300);

// 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
counter.getHits(301);
进阶:

如果每秒的敲击次数是一个很大的数字，你的计数器可以应对吗？
'''
from collections import deque
'''
思路：队列
设一个最长300的队列，内部元素为(时间戳,敲击总数)的数对
hit函数会查看队尾的元素的时间戳是否与参数相同，如果相同，更新；如果不同，添加一个新的数对
getHits函数会将队头的敲击总数减去队尾的敲击总数得到5分钟内的敲击数

上述2个函数在调用时都要删除队头超过5分钟的数对。

时间复杂度：队列长度最长300，2个函数都是O(1)
'''


class HitCounter:
    def __init__(self):
        self.queue = deque()
        self.lastHits = 0

    def ensureTime(self, timestamp):
        lastTime = timestamp - 300
        while self.queue and self.queue[0][0] <= lastTime:
            self.lastHits = self.queue.popleft()[1]  # 去掉超时的敲击，并更新去掉的敲击次数

    def hit(self, timestamp: int) -> None:
        if self.queue:
            if self.queue[0][0] == timestamp:  # 与最近一次敲击的时间相同，修改队尾
                self.queue.append((timestamp, self.queue.pop()[1] + 1))
            else:  # 时间不同，添加
                self.queue.append((timestamp, self.queue[-1][1] + 1))
        else:  # 队列为空，添加一个敲击次数为0的数对
            self.queue.append((timestamp, 1))
        self.ensureTime(timestamp)  # 去掉超时的敲击

    def getHits(self, timestamp: int) -> int:
        self.ensureTime(timestamp)  # 去掉超时的敲击
        if self.queue:  # 结果为最近一次敲击总数-去掉的敲击次数
            return self.queue[-1][1] - self.lastHits
        return 0


c = HitCounter()
c.hit(1)
c.hit(2)
c.hit(3)
print(c.getHits(4))
c.hit(300)
print(c.getHits(300))
print(c.getHits(301))
